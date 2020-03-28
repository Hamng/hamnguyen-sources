#!/bin/bash

#
# What this script does:
#   This script launches multiple concurrent instances of fio,
#   one for each device/filename to be tested.
#   Then within each instance, loop thru the specified blocksizes.
#   Then for each blocksize, run many runs.
#
# How to use it:
#   fio_write.sh  '/dev/nvme{0..3}n1'  ['{log2blkszfirst..log2blkszlast}'  ['run_{first..last}'  [...]]]
#
# Requirements:
#  (1.	Run as root since 1st arg is typically a block device.)
#   2.	Will create a directory hierarchy in the curdir to save logs,
#	so curdir needs to be writable by the effective user (typically "root").
#   3.	Need a *.fio in the same directory as this script, whose basename
#	matches the basename of this script; e.g. 'fio_write'
#	This *.fio file should specify fio params; especially 'readwrite=<str>',
#	but should NOT specify any 'filename=' param
#
# Args:
#   1.	REQUIRED: device(s)/filename(s) to run. To specify multiple device(s)/filename(s),
#	must quote them, and can use a Bash sequence expression such as:
#	/dev/nvme5n1, '/dev/nvme{0..7}n1', '/dev/nvme0n{9..2..3}', '/dev/nvme[0,1,3]n1'
#	or space-separated devices '/dev/nvme9n1 /dev/nvme0n2 /dev/nvme6n2'
#   2.	Blocksizes to be tested, specified as log2 of the blocksizes;
#	e.g. for log2 == 13, blocksize = (1 << log2) == 8k.
#	Similarly, can use a Bash sequence expression to specify multiple blocksizes.
#	Default: '21 20 {17..12}' to test 2M, 1M, then 128KiB down to 4KiB.
#   3.	Number of runs to test for each blocksize.  Default: 'run_{1..3}' for 3 runs
#   4.	Additional fio options to be passed on as-is.
#	Trickery: "eval $(fio --showcmd *.fio) blah..." expands the settings within the
#	*.fio jobspec to be command-line options, which could then be overriden by "blah..."
#	These go after settings in the jobspec, and --filename= and --bs= settings,
#	so could be used to override earlier settings
#   5.	Preset fio options, which can be overridden via command-line:
#	--idle-prof=percpu	Report system and per-CPU idleness
#	NOPE, DON'T add this flag: it'll drop %idle to 0 (on NVMEoF client/initiator)!
#   6.	Some useful fio options:
#	--readonly		Seem NOT valid within a job file, so can ONLY specify on command-line???
#	--numjobs=N		spawn N jobs. To measure CPU & memory usage properly, should accept the
#				default --numjobs=1. Otoh, to get the max bandwidth, use --numjobs=2.
#				(Then total IO = N x the size setting in *.fio).
#	--loops=N		Loop internally N times; hence total IO will be Nx
#	--description='...'	Output a textual description per job.
#
# Notes:
#   1.	To loop thru from 1 to N consecutive devices, use:
#	(Hint: copy-n-paste the 'echo' command to 'eval' to preserve quotations.)
#
#	    for n in {0..7}; do echo "..../fio_write.sh" "'/dev/nvme{0..$n}n1'"; eval ..../fio_write.sh "'/dev/nvme{0..$n}n1'"; done
#
#	That'd run this script 8 times as:
#	    fio_write '/dev/nvme{0..0}n1'		# 1 device
#	    fio_write '/dev/nvme{0..1}n1'		# 2 devices
#		...
#	    fio_write '/dev/nvme{0..7}n1'		# 8 devices
#	(Why need to 'eval'? Need to eval "'/dev/nvme{0..$n}n1'" to an actual number
#	so it'd become: '/dev/nvme{0..X}n1')
#
#   2.	To collect the relevant performance so can paste into a spreadsheet:
#
#	    egrep -r ' *WRITE' ?_devices | sed -e 's#\([/_(),]\)# #g' | sort -k 5n | awk '{$14=0+$14; print}' | xclip -i
#
#	Grep for lines begin with 'WRITE', and showing filename, e.g.:
#		1_devices/write/blocksize_4KiB/run_1/fio_write_nvme0n1.log:  WRITE: bw=416MiB/s (436MB/s), ...
#	'sed' replaces most punctuation marks with spaces:
#		1 devices write blocksize 4KiB run 1 fio write nvme0n1.log:  WRITE: bw=416MiB s  436MB s ...
#	Sort on the 5th column (blocksize) as numeric.
#	Awk converts the 14th column to numeric; e.g. "436MB" ==> 436
#	xclip copies stdout to the clipboard so can be pasted
#
#	In case someone is vi'ing an fio*.log file, which creates a hidden .fio*.log.swp,
#	the 'egrep -r' would fail since it also pickups the hidden files then show as 'Binary files ...'
#	In that case, use:  grep -H ' *WRITE' ?_devices/*/blocksize_*/run_*/fio*.log ...
#
#   3.	From an mpstat*.log, a typical question might be: how many CPUs to saturate ...?
#	That could be roughly calculated from the '%idle' (last) column of CPU=='all' as:
#	    %busy_all_per_cpu	= (100 - %idle_all)
#	    %busy_all_total	= %busy_all_per_cpu * num_cpus_total	(in % unit)
#	    num_cpus_used	= %busy_all_total / 100
#				= (1 - %idle_all / 100) * num_cpus_total
#	We can use the following 1-liner awk:
#	    awk '/ all / {print (100 - $NF) * NUM_CPUS / 100}' < mpstat*.log | xclip -i
#	(Might need to remove the last line since it wrongly pickups the 'Average:' lines.)
#
#	Then iterate thru all *_devices to pause+paste for individual blocksize with:
#	    for n in {1..8}_devices; do for b in 4 8 16 32 64 128; do awk '/ all / {...above...}' < $n/*/*_${b}KiB/mpstat*.log | xclip -i; read -p "$(echo -e \\nPaste for $n/*/*_${b}KiB/mpstat*.log), then press Enter to continue"; done; done
#
#	Or showing all:
#	    grep ' all ' ?_devices/*/blocksize_*/mpstat*02.log | sed 's#[_/]# #g' | sort -k 5n | awk '{print $5, ...above...}' | xclip -i
#
#   4.	Another common way to parse mpstat log is to plot the "# of CPUs used to saturate device"
#	That means for each time marker, sum the %sys (5th) columns, then count non-0 values,
#	then average over non-0 values only. If there's at least 1 non-0 value, plot the
#	"Average-of-non-0-%sys / 100" which is considered to be the "number of CPUs used
#	to saturate device".  (This probably applies to 1 device only?)
#	Use the helper AWK script in this same dir as:
#
#	    awk -f mpstat_parse_sys.awk < mpstat*.log | xclip -i
#
#	Paste the output to Excel, then plot "Average-of-non-0-%sys / 100"
#	Caveat: prefix LC_TIME=en_UK.utf8 to mpstat to log time in 24-hour format (no AM/PM)
#
#   5.	To capture %Memused: for each '%memused' heading line,
#	drop it, read the next line, then output the 5th field:
#	    awk '/ %memused / {getline; print $5}' < sar*.log | xclip -i
#
#	Then iterate thru all *_devices to pause+paste for individual blocksize with:
#	    for n in {1..8}_devices; do for b in 4 8 16 32 64 128; do awk '/ %memused / {getline; print $5}' < $n/*/*_${b}KiB/sar*.log | xclip -i; read -p "$(echo -e \\nPaste for $n/*/*_${b}KiB/sar*.log), then press Enter to continue"; done; done
#
#	Or showing all:
#	    egrep --no-group -A1 '%memused' 1_devices/write/blocksize_*/sar,msl-lab-ads02.log | sed -e 's#\([/_]\)# #g' | sort -k 5n | awk '{getline; print $5, $10}' | xclip -i
#	Grep for '%memused', and display the next line, but no separating '--' line:
#		1_devices/write/blocksize_128KiB/*:08:06:10 PM kbmemfree kbmemused %memused ...
#		1_devices/write/blocksize_128KiB/*:08:06:11 PM 154624700  92744708 37.25 ...
#	'sed' replaces most punctuation marks with spaces:
#		1 devices write blocksize 128KiB *:08:06:10 PM kbmemfree kbmemused %memused ...
#		1 devices write blocksize 128KiB *:08:06:11 PM 154624700  92744708 37.25 ...
#	Sort on the 5th column (blocksize) as numeric.
#	Awk skips the heading, then print 5th column (blocksize), and 10th (%memused)
#
#   6.	And here's an impossibly long 1-liner to test on NVMEoF client and target
#	Prerequisite: root-on-client must be able to ssh root@TARGET without being prompted.
#	As root on client/initiator
#	cd to a dir sharing with target
#	ssh -f TARGET /bin/bash -cx '"uname -a; date; cd path_sharing_with_client; mpstat -P ALL 1 > mpstat,$(uname -n).log 2>&1 & sar -r -S 1 > sar,$(uname -n).log 2>&1 &"' & path/to/fio_write.sh dev ...; ssh TARGET /bin/bash -cx '"uname -a; date; pkill -INT mpstat; pkill -INT sar"'



script_0=${0##*/}				# basename $0
script_0=${script_0%.*}				# strip off .sh suffix
script_words=(${script_0//_/ })			# tokenize using '_'
script_command=${script_words[0]}		# main command; i.e. "fio"
script_subcommand=${script_words[1]}		# subcommand; i.e. "write"
#script_param=${script_words[2]}		# parameter; i.e. "nvme0n1"
script_path=$(readlink -f $0)
script_path=${script_path%/*}			# dirname $0
#echo "_words=${#script_words[*]}<${script_words[*]}>"

if [[ $# -lt 1 ]]; then
    echo "${script_0}.sh '/dev/nvme{F..L}n1' ['{log2blkszF..log2blkszL}' ['run{F..L}' ...]]" 1>&2
    exit 1
fi

filename_list=($(eval echo $1))
shift
bs_list=($(eval echo ${1:-"21 20 {17..12}"}))
shift
run_list=($(eval echo ${1:-"run_{1..3}"}))
shift

#echo "remainder=<$@>"
#set -o xtrace

# Global var to be set when a thread aborted
aborted=0

function fio_single_filename() {
    local run logfile line1 testop bs_kib stat logdir exit_status
    # log2blocksize filename ...
    # ${filename##*/}: basename of filename; e.g. "nvmeXnY" from $1="/dev/nvmeXnY"
    #for bslog2 in ${bs_list[*]}
    #do
	declare -r -i bs=$((1 << ${1} >> 10))			# to bytes, then to KiB
	shift
	declare -r filename=${1}
	shift
	for run in ${run_list[*]}
	do
	    printf -v logfile "%s_%s.log" ${script_0} ${filename##*/}
	    printf "%(%F %T)T, %s/%s: %s %s %s %s %s %s %s\n\n" -1 ${run} ${run_list[-1]} "$(${script_command} --showcmd ${script_path}/${script_0}.fio)" "--filename=${filename}" "--bs=${bs}k" "${*}" "&>>" ${logfile} |& tee ${logfile}

	    # Was showing a run as: "run_$cur/${#run_list[*]}", but that looks weird
	    # if run_first != 1, then a run might show up as "run_X/Y" where X > Y.
	    # So now using "run_$cur/${run_list[-1]}"
	    # Punted: if using decreasing sequence {large..small}, or non-sequential
	    # Might need to unmount ${filename}, but typically only partition(s)
	    # are mounted, so unsure how to determine which partition(s) to unmount.
	    #umount -fv ${filename} 2> /dev/null

	    eval $(${script_command} --showcmd ${script_path}/${script_0}.fio) --filename=${filename} --bs=${bs}k "${@}" "&>>" ${logfile}

	    exit_status=$?

	    # TO DO: trap for SIGTERM (15): when testing a large number of devices (> 10),
	    # an inst might abort with signal 15 since can't launch jobs.  Then:
	    #  1. This entire script is aborted and reporting "Terminated" on stdout.
	    #  2. The offending jobs still pending.
	    # So need to trap for then possibily handling it by:
	    #  3. "pkill -9 ${script_command}" to kill all pending jobs
	    #  4. "continue" here to continue with the next run, hence skipping a run.

	    # Parse the 1st fio output line (== line #3) containing test params, removing commas ',':
	    # write-test: (g=0): rw=write, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=1024
	    # line1[2]="rw=write": testop: use 'expr' to keep only after the '=' char
	    line1=($(sed -n 3p ${logfile} | tr -d ','))
	    testop="$(expr match ${line1[2]} '.*=\(.*\)')"
	    # awk on line1[6]="128KiB-128KiB" which is blocksize for (W):
	    # -F '-': use '-' as a separator
	    # t=substr($NF,0,length($NF)-1): set t to the last field, stripping out the ending "B"
	    # sub("\\.[[:digit:]]+"..): remove all digits after-and-including dot; e.g. "16.0Ki" => "16Ki"
	    # (t+0): convert t to a number by stripping out all non-digit suffix
	    # if ((t+0)==t): if the converted t == the original t, meaning t is all numeric;
	    # (i.e. no "Ki", "Mi", "Gi"), then scale down+append "Ki" suffix.
	    # Finally, print t with a "B" suffix adding back on.
	    # TO-DO: need to normalize all "*iB" to "KiB"
	    bs_kib=$(echo ${line1[6]} | awk -F '-' '{t=substr($NF,0,length($NF)-1);sub("\\.[[:digit:]]+","",t); if ((t+0)==t) {t=(int(t/1024))"Ki"} print t"B"}')

	    # Parse the line following the 'Disk stats' line:
	    # Disk stats (read/write):
	    #   nvme0n2: ios=43/204800, merge=0/0, ticks=15/42823, in_queue=42657, util=98.66%
	    # awk -F:	Run awk with colon (':') as the field delimiter
	    #	Select the 'Disk stats' line; drop it; read the next line; print 1st field
	    # stat=(): to trim off leading whitespaces
	    stat=($(awk -F: '/^Disk stats/ {getline; print $1}' < ${logfile}))

	    if ((${exit_status})); then
		printf "\n\n%(%F %T)T, %s/%s: %s %s %s %s\n\n" -1 ${run} ${run_list[-1]} "${script_command} ..." "--filename=${filename}" "--bs=${bs}k" "ABORTED" | tee --append ${logfile}
	    fi

	    printf -v logdir "%u_devices/%s/blocksize_%s/%s" ${#filename_list[*]} ${testop} ${bs_kib} ${run}
	    mkdir -p ${logdir} 2> /dev/null
	    mv -fv ${logfile} ${logdir}/${script_command}_${testop}_${stat[0]}.log

	    if ((${exit_status})); then
		# Fio exited with a non-0, which is typically caused by a user-abort
		# so abort the current loop. Also, set the global ${aborted} to non-0
		aborted=${exit_status}
		break
	    fi

	done

	# As a side-effect/return_value, leave a symlink for caller to move stuff into
	# Caveat: the commands below are executed in multiple concurrent processes
	rm -fv symlink_to_last_run
	ln -sfv ${logdir} symlink_to_last_run
    #done
}

# Relax permissions
umask 002


for bslog2 in ${bs_list[*]}
do
    stat_pids=()
    pkill -INT mpstat
    LC_TIME=en_UK.utf8 mpstat -P ALL 1 > mpstat,$(uname -n).log 2>&1 &
    stat_pids+=($!)

    pkill -INT sar
    sar -r -S 1 > sar,$(uname -n).log 2>&1 &
    stat_pids+=($!)

    # Launch 2nd to last instances in background
    # Caveat: the individual insts might be running *out-of-sync*;
    # i.e. some insts are running iteration 'run_X' while other are running 'run_Y'
    # TO-DO: to keep all insts running in lock-step, might need to move the
    # "for run ..." loop here, then background the actual "fio" steps
    pids=()
    for fname in ${filename_list[*]:1}
    do
	fio_single_filename ${bslog2} ${fname} "${@}" &
	pids+=($!)
    done

    # Run the first instance in foreground
    fio_single_filename ${bslog2} ${filename_list[0]} "${@}"

    if [[ ! -z $pids ]]; then
	printf "\n\n%(%F %T)T: waiting for %u PIDs (%s) to complete\n" -1 ${#pids[*]} "${pids[*]}"
	wait "${pids[@]}"
    fi

    # kill -INT (== Ctrl-C) to log the ending "Average" summary
    kill -INT ${stat_pids[*]} 2> /dev/null
    wait ${stat_pids[*]} 2> /dev/null

    # symlink_to_last_run is a symlink created as a side-effect/return_value
    # from fio_single_filename(), so move the *.log there
    # Leave the symlink in-place in case needed by an external process
    mv -fv mpstat*.log sar*.log symlink_to_last_run
    #rm -fv symlink_to_last_run

    if ((${aborted})); then
	# Some entities set this "wanting to abort" flag, so abort
	break
    fi

done
