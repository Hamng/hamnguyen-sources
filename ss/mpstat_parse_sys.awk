
#
# This AWK script parse output from 'mpstat -P ALL 1' which should look like:
#
#Linux 4.14.79 (msl-wisray-lt) 	01/28/20 	_aarch64_	(8 CPU)
#
#13:36:18     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
#13:36:19     all    0.00    0.00    0.12    0.12    0.00    0.00    0.00    0.00    0.00   99.75
#13:36:19       0    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       1    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       2    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       3    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       4    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       5    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       6    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#13:36:19       7    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#
#13:36:19     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
#
# It finds a group whose %sys column (5th) contains non-0 entries:
#	it then prints the time, count, sum, and average
# Enhancement: pass in "5" as a var instead of hard-wiring
# Caveat: CentOS mpstat adds and extra 2nd column for AM/PM. Workarounds:
#  a.	Prefix mpstat with LC_TIME=en_UK.utf8 to log time in 24-hour format.
#  b.	Or, for a log already containing AM/PM, before passing to this AWK script, discard 2nd column with:
#		 awk '{$2=""; print}'

$2 == "all" && $1 ~ /^[0-9]/ {
    # A group begins with 'CPU=all' , so mark the time, then init vars
    # Why adding 1st field starts wiht a digit? To ignore the 'Average' lines at the end
    time  = $1
    count = 0
    sum   = 0

    # Done with 'all', read the next line (typically 'CPU==0')
    not_eof = getline
    while (not_eof && NF > 0) {
	# Loop while not at an empty line
	if ($5 != 0.00) {
	    # If the %sys column is non-0, bump the count, and sum up
	    count++
	    sum += $5
	}
	not_eof = getline
    }

    if (count != 0) printf("%s: %u non-idle cpus, %.2f total %%sys, %.3f avg %%sys\n",
			   time, count, sum, sum / count)
}
