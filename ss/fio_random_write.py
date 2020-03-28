#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:47:24 2020

@author: ham.nguyen

VERY IMPORTANT:
    Spyder/IPython messes up logging (e.g. messages not shown in desired format)
    Woraround: import+reload logging before everything else.
    Sigh, reload isn't a builtin for Python 3, so need to import from importlib

"""

import logging
from importlib import reload
reload(logging)

import sys
import os
import argparse
#import logging
import subprocess
import threading
import signal
import time

logchoices = ['info', 'debug']

basenm = os.path.splitext(os.path.basename(sys.argv[0]))[0]
prefix = basenm.split('_', 1)[0]
logger = logging.getLogger(basenm)
uname_n = os.uname()[1]
rw_action = None

mpstat_command = 'mpstat -P ALL 1'.split()
mpstat_logfile = 'mpstat,' + uname_n + '.log'
sar_command    = 'sar -r -S 1'.split()
sar_logfile    = 'sar,' + uname_n + '.log'


def background_redirect_stdout(command, logfile, dryrun=False):
    logger.debug(' '.join(command + ['>', logfile, '2>&1', '&']))
    if not dryrun:
        return subprocess.Popen(command, stderr=subprocess.STDOUT,
                                stdout=open(logfile, 'w'))


def do_1_device(blocksize_KiB, run, device, foreground=True, dryrun=False,
                fio_settings_from_file=None, fio_args=None, *args, **kwargs):
    threading.current_thread().name = " ".join([device, rw_action])
    device = '/dev/' + device
    if fio_args is None:
        fio_args = []
    fio_args = fio_settings_from_file + \
                ['--filename=' + device, '--bs=' + str(blocksize_KiB) + 'k'] + \
                fio_args
    logger.info(' '.join([run + ':'] + fio_args))
    time.sleep(45)


def do_1_run(blocksize_KiB, run, devices=None, dryrun=False, *args, **kwargs):
    for dev in devices[:-1]:
        # caller already set in **kwargs, so now passing on:
        # fio_settings_from_file[], fio_args[]
        do_1_device(blocksize_KiB, run, device=dev, foreground=False,
                    dryrun=dryrun, *args, **kwargs)

    # caller already set in **kwargs, so now passing on:
    # fio_settings_from_file[], fio_args[]
    do_1_device(blocksize_KiB, run, device=devices[-1], foreground=True,
                dryrun=dryrun, *args, **kwargs)
    #wait for all threads


def do_1_blocksize(log2blocksize, runs=None, do_mpstat=True,
                   do_sar=False, dryrun=False, *args, **kwargs):
    if do_mpstat:
        mpstat_proc = background_redirect_stdout(mpstat_command,
                                                 mpstat_logfile, dryrun=dryrun)
    if do_sar:
        sar_proc    = background_redirect_stdout(sar_command,
                                                 sar_logfile, dryrun=dryrun)

    # Too bad, anything smaller than 1k will yield bs_KiB=0
    bs_KiB = (1 << log2blocksize) >> 10
    for run in runs:
        # caller already set in **kwargs, so now passing on:
        # devices[], fio_settings_from_file[], fio_args[]
        do_1_run(blocksize_KiB=bs_KiB, run=run, dryrun=dryrun, *args, **kwargs)

    if do_mpstat:
        logger.debug(' '.join(['pkill', '-INT', 'mpstat']))
        if not dryrun:
            mpstat_proc.send_signal(signal.SIGINT)
            mpstat_proc.wait()
    if do_sar:
        logger.debug(' '.join(['pkill', '-INT', 'sar']))
        if not dryrun:
            sar_proc.send_signal(signal.SIGINT)
            sar_proc.wait()

    #mv *.log symlink_to_last_run


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="For each power-of-2 blocksize being iterated thru,"
        " this script launches multiple concurrent '" + prefix
        + "' instances, one for each specified (NVME) device."
        " Then for each blocksize, repeat the set of '" + prefix
        + "' instances for several runs"
        " (typically to obtain average performance)."
        )
    # Caveat: non-options must stay together, usually at the end
    parser.add_argument('devices', metavar='dev', nargs='+',
    # Hack alert: to use Bash to specify multiple blocksizes:
    # eval  this_module.py  --log2blocksize="'"{21..13}"'"  ...
                        help="(NVME) device(s) to be tested"
                        " e.g. 'nvme0n1'; without the '/dev/' prefix")
    parser.add_argument('--log2blocksize', '-b', action='append',
                        #default=['21 20 17 16 15 14 13 12'],
                        help="base2 logs of the blocksizes to be tested;"
                        " e.g. '14' for a 16KiB blocksize == 14^2 == (1 << 14)."
                        " Can specify multiple times to be accumulated."
                        " Can be specified as a quoted list of log2blocksizes"
                        " separated by spaces."
                        " Default: '21 20 17 16 15 14 13 12'")
    parser.add_argument('--run', '-r', action='append',
                        help="labels for the runs to loop thru."
                        " Can specify multiple times to be accumulated."
                        " Default: 'run_1 run_2 run_3'")
    parser.add_argument('--' + prefix + '_file', '-f', type=argparse.FileType('r'),
                        help="The (job)file to read '" + prefix + "' parameters"
                        "from. Default: " + basenm + '.' + prefix)
    parser.add_argument('--' + prefix + '_args', help="pass options as-is to '"
                        + prefix + "' (should quote options)")
    parser.add_argument('--no_mpstat', action='store_true',
                        help="don't launch an 'mpstat' command."
                        " Default: do launch 'mpstat' (in background)")
    parser.add_argument('--remote_mpstat',
                        help="Remote host:path to launch 'mpstat'"
                        " (in background), and store a mpstat*.log in")
    parser.add_argument('--sar', action='store_true',
                        help="launch a 'sar' command."
                        " Default: don't launch 'sar' (in background)")
    parser.add_argument('--remote_sar',
                        help="Remote host:path to launch 'sar'"
                        " (in background), and store a sar*.log in")
    parser.add_argument('--dryrun', action='store_true',
                        help='only show actions/commands that would run')
    #parser.add_argument('--verbose', '-v', action='count', default=0)
    parser.add_argument('--loglevel', '-l', choices=logchoices, default='info',
                        help="either 'info' (default), or 'debug' (more verbose)")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    args = parser.parse_args()

    args.devices = sorted(set(args.devices))
    #print('devices=', args.devices)
    if args.log2blocksize:
        if not args.log2blocksize[-1].isdigit():
            # if specified as a quoted space-separated list of log2blocksizes
            args.log2blocksize = args.log2blocksize[-1].split()
        args.log2blocksize = list(map(int, args.log2blocksize))
    else:
        args.log2blocksize = [21, 20, 17, 16, 15, 14, 13, 12]

    if not args.run:
        args.run = ['run_1', 'run_2', 'run_3']

    if args.fio_file:
        # extracting the .name member from an argparse.FileType object
        args.fio_file = args.fio_file.name
    else:
        # Default to be in the same fully qualified dirname of sys.argv[0]
        args.fio_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                                     basenm + '.' + prefix)
    if args.fio_args:
        args.fio_args = args.fio_args.split()
    else:
        # Make it an empty list so later can append to other lists
        args.fio_args = []

    # Problem: for each run within Spyder/IPython, a log entry would be
    #   dup'ed; e.g. 1st run, it shows up once; 2nd: it shows up twice;
    #   Nth run: N times; till restarting the kernel.
    #   No such problem when running stand-alone outside Spyder.
    # Cause: in Spyder, there're lots of log handlers pre-added, then for
    #   each run, our handler here will be addHandler()'ed again, hence dup
    # Fix: clear logging.Logger.manager.loggerDict
    #print(logging.Logger.manager.loggerDict.keys())
    logging.Logger.manager.loggerDict = {}
    #logging.basicConfig(format="xvbfdd fg dfgdf %(asctime)s, %(message)s")
    # Caveat: .getLogger().setLevel() so to make it work for IPython/Spyder
    #logging.basicConfig(level=logmap[args.loglevel])
    logger.setLevel(getattr(logging, args.loglevel.upper(), None))

    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, args.loglevel.upper(), None))
    ch.setFormatter(logging.Formatter('%(asctime)s [%(threadName)s]: %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S'))
    # add the handlers to logger
    logger.addHandler(ch)

    if sys.version_info.minor > 6:
        # Ouch: 'text' and 'capture_output' work only with Python 3.7 and newer
        fio_settings = subprocess.run([prefix, '--showcmd', args.fio_file],
                                      text=True, capture_output=True,
                                      check=True).stdout.strip().split()
    else:
        fio_settings = subprocess.check_output([prefix, '--showcmd', args.fio_file]
                                          ).decode().strip().split()

    # Collect all '--rw=' or '--readwrite=' settings in fio_settings+fio_args
    # If exists, use the last setting, split+keep only after the last '='
    rw_action = [e for e in fio_settings + args.fio_args
                 if e.startswith('--rw=') or e.startswith('--readwrite=')]
    if len(rw_action):
        rw_action = rw_action[-1].rsplit('=', 1)[-1]
    else:
        rw_action = ''
    threading.current_thread().name = " ".join([args.devices[-1], rw_action])

    logger.debug(args)
    logger.debug(" ".join([prefix, 'settings:'] + fio_settings))

    for log2blocksize in args.log2blocksize:
        do_1_blocksize(log2blocksize, runs=args.run, devices=args.devices,
                       fio_settings_from_file=fio_settings, fio_args=args.fio_args,
                       do_mpstat=not args.no_mpstat, do_sar=args.sar,
                       dryrun=args.dryrun)
