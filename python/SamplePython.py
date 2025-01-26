#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Ham Nguyen

"""

import sys
import os
import argparse
import logging

class CatchAll(object):
    def meth_a(self, arg):
        print(f"{self.__class__.__name__}.meth_a(self@0x{id(self):X}, arg=0x{id(arg):X})")

    def meth_two(self, arg):
        print(f"{self.__class__.__name__}.meth_two(self@0x{id(self):X}, arg=0x{id(arg):X})")

    def c_meth(self, arg):
        print(f"{self.__class__.__name__}.c_meth(self@0x{id(self):X}, arg=0x{id(arg):X})")

class MyClass(object):
    def __init__(self, a=0, b=0):
        if sys.platform == 'darwin':
            print(f"{self.__class__.__name__}.{sys._getframe(0).f_code.co_name}(a={a}, b={b})")
        else:
            # MicroPython doesn't support sys._getframe
            print(f"{self.__class__.__name__}.__init__(a={a}, b={b})")
        self.varA = a
        self.varB = b
        self._catchall = CatchAll()
        print(f"self@0x{id(self):X}, ._catchall@0x{id(self._catchall):X}")

    def get_by_name(self, attrname: str):
        # Testing getting an attribute by name at runtime
        return getattr(self, attrname)

    def __getattr__(self, attrname: str):
        # typical implementation
        #return getattr(self._catchall, attrname)
        # Special implementation
        attr = getattr(self._catchall, attrname)
        if False and callable(attr):
            # This does NOT work completely!
            print(f"'.{attrname}'")
            return attr(self._catchall)
        else:
            return attr

    def __del__(self):
        if sys.platform == 'darwin':
            print(f"{self.__class__.__name__}.{sys._getframe(0).f_code.co_name}()")
        else:
            # Bug: MicroPython does NOT call this when destroying an object
            print(f"{self.__class__.__name__}.__del__()")

def myfunc():
    print("\n")
    my_obj = MyClass(12, 64)
    print(".varA=", my_obj.get_by_name("varA"))
    print(".varB=", my_obj.get_by_name("varB"))
    my_obj.meth_a(1)
    my_obj.meth_two(2)
    my_obj.c_meth(3)


if __name__ == '__main__':
    # VERY IMPORTANT: MUST call .basicConfig(level=logging.INFO) else no log messages!
    # Because the default is level=logging.WARNING hence *NO* INFO/DEBUG messages!
    logging.basicConfig(format='%(levelname)s: %(message)s')
    # Save old loglevel, temporarily set it to DEBUG to show the debugs,
    # then restore the old loglevel
    # Totally mysterious hack: in EFI, if import AppleBaseWrapper,
    # then each logging would appear TWICE?????
    # Workaround: pop a (log) handler from the current logger.
    # That seems to work in macOS too, so no need to test for EFI
    old_loglevel = logging.getLogger().level
    logging.getLogger().setLevel(logging.DEBUG)
    #logging.getLogger().handlers.pop()
    logging.debug(f"sys.path[]: {len(sys.path)} {sys.path}")
    logging.debug(f"argv[]: {len(sys.argv)} {sys.argv}")
    logging.debug("file='" + __file__ + "'")

    if sys.platform == 'darwin':
        ContainerName = os.path.basename(sys.argv[0])
    else:
        # sys.platform == 'uefi'
        # sys.argv[0]='prefix\\ContainerName\\ScriptName.py'
        # .rsplit(,2) => ['prefix', 'ContainerName', 'ScriptName.py']
        ContainerName = sys.argv[0].rsplit('\\', 2)[1]
        logging.debug('ContainerName=<' + ContainerName + '>')

    logging.getLogger().setLevel(old_loglevel)

    # type= is used to validate argument in 'darwin' (but ignored in non-darwin) so need to provide a valid type
    parser = argparse.ArgumentParser(description="A sample Python script to be launched from Smokey")
    parser.add_argument("--AdditionalPdca", dest="AdditionalPdca", type=str, default=None, help=" Location for the final result")
    parser.add_argument("--fail", dest="exit_as_failed", action="store_true", default=False, help=f"If specified, force {ContainerName} to exit as FAILED")
    parser.add_argument("--intval", dest="intval", type=int, default=6, help="an int value, default=6")
    parser.add_argument("--val0", dest="val0", type=int, default=0, help="an int value, default=0")
    parser.add_argument("--val0_abc", type=str, default=None, help=" a string option sharing the same 'val0' prefix")
    # if not specified, will take (int) value in default=. If specified, will be forced to (int) value in const=
    # The default dest is the same as the optname, stripping off all '-' prefix, and convert remaining '-' to '_'
    parser.add_argument("--const-int", action="store_const", const=17, default=92, help="if specified, force to 17. Else, default to 92.")
    # Weird: macOS does NOT accept type=str for action="store_const" although it's logically correct???
    parser.add_argument("--str-const", action="store_const", const="enabled", default="whatelse", help="if specified, force to 'enabled'. Else, default to 'whatelse'.")
    #parser.add_argument("--debug", "--verbose", dest="verbose_level", type=int, default=0, help=" A higher verbose/debug value shows more messages")
    parser.add_argument("-d", "--debug", "--verbose", action="store_true", default=False, help=f" If specified, set the loglevel to DEBUG to show more messages")
    parser.add_argument("--listof", help='Use space to separate individual items, then double-quote the entire list; e.g. "xy 12 vw"')
    parser.add_argument("--want-3-item", nargs=3, help=f" If specified, must provide 3 space-separated args.")

    # From Smokey, to pass additional opt+arg:
    # smokey ... --args "PyArgs='--opt1 arg1 --opt2 arg2 ...'"
    # Of course, must parser.add_argument("--opt1", ...)
    # remainder is a catchall for all positional args that aren't preceded by an --optX
    # Fyi, sys.argv[] remains intact
    # Reg argparse, either:
    #  a. Don't use argparse at all
    #  b. Else, MUST handle ALL options!
    #parser.add_argument("remainder", nargs='*', help="unparsed rest of positional args")
    # Or, if there're many possible catchall --optX, then prefix each with '--' as usual
    # but user MUST explicitly specify --optX before the list
    # A slight difference when a catchall optname is NOT specified:
    #   nargs='*': args.optname = []
    #   nargs='+': args.optname = None
    parser.add_argument("--rem1", dest="remainder1", nargs='+', help=" unparsed rest of 1+ positional args")
    #parser.add_argument("--rem2", dest="remainder2", nargs='*', help=" unparsed rest of positional args")
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

        # Here's a VERY HACKY way to assign vars with the matching one in args[]
        # i.e. [var=args.var for var in dir(args)]
        # Since it's hacky, do this only in EFI and when --debug
        # Caveat: the globals() version might NOT work for locals()
        # When an option has multiple aliases, only the 1st double-dash option is created in args[]
        # e.g. '-d' and '--verbose' are aliases for '--debug' but only args.debug exists
        for elem in sorted(dir(args)):
            if not elem.startswith('_'):
                # filter-out the pre-defines that are prefixed with '_'
                #print(f'{elem}=args.{elem}')
                #print('f{elem}=args.{elem}; print(f"{elem}=' + '{' + f"{elem}" + '}")')
                #exec(f'{elem}=args.{elem}; logging.debug(f"{elem}=args.{elem}=' + '{' + f"{elem}" + '}")')
                if sys.platform == 'darwin':
                    # only MacOS has __getattribute__()
                    # Too bad, the args.{elem} version preserves its type;
                    # otoh, the __getattribute__() version forces most to be a string
                    # On the RHS, if removing the bracketing double-quotes,
                    # it'd preserve the type, but fail if the rhs string has an embedded space. Sigh!
                    #logging.debug(f'args.getttr("{elem}")="%s"', args.__getattribute__(f"{elem}"))
                    exec(f'{elem}="' + str(args.__getattribute__(f"{elem}")) + '"')
                else:
                    exec(f'{elem}=args.{elem}')
                #globals()[f'{elem}'] = eval(f'args.{elem}')
                logging.debug(f"{elem}=args.{elem}=%s, %s", eval(f'{elem}'), type(eval(f'{elem}')))

    logging.debug(f"dir(args)={dir(args)}, args={args}")

    AdditionalPdca = args.AdditionalPdca
    if AdditionalPdca:
        # set if launched from Smokey
        DirPath, Basename = AdditionalPdca.rsplit("\\", 1)
        logging.debug('AdditionalPdca=<' + AdditionalPdca + '>')
        logging.info('DirPath=<' + DirPath + '>')
        logging.info('Basename=<' + Basename + '>')

    logging.info(f"intval={args.intval}, {type(args.intval)}")
    if args.val0:
        logging.info(f"specified: val0=<{args.val0}>, int={int(args.val0) + 0}, {type(args.val0)}")
    else:
        logging.info(f"default: val0={args.val0}, {type(args.val0)}")
    logging.info(f"val0_abc='{args.val0_abc}', {type(args.val0_abc)}")
    logging.info(f"const-int={args.const_int}, {type(args.const_int)}")
    logging.info(f"str-const='{args.str_const}', {type(args.str_const)}")
    #print(f"verbose_level={int(args.verbose_level) + 0}, {type(args.verbose_level)}")

    listof = args.listof
    if listof is None:
        logging.info(f"listof: {listof}")
    else:
        listof = listof.split()
        logging.info(f"listof[]: {len(listof)} {listof}")

    item3 = args.want_3_item
    if item3 is None:
        logging.info(f"want-3-item: {item3}")
    else:
        logging.info(f"want-3-item[]: {len(item3)} {item3}")

    remainder = args.remainder1
    if remainder is None:
        logging.info(f"remainder: {remainder}")
    else:
        logging.info(f"remainder[]: {len(remainder)} {remainder}")

    if len(sys.argv) < 2:
        logging.warning(f"Need at least 1 command-line arg")
        if sys.platform != 'darwin':
            parser.usage(True)

    myfunc()
    if sys.platform != 'darwin':
        logging.warning(f"MicroPython does NOT call __del__() when destroying an object, sigh!\n\n")

    print("\n")
    if bool(args.exit_as_failed):
        logging.error(f"{ContainerName} sys.exit(1) since --fail {type(args.exit_as_failed)} specified")
        sys.exit(f"{ContainerName} failed")
    else:
        logging.info(f"--fail={args.exit_as_failed}, {type(args.exit_as_failed)} NOT specified ==> normal exit")
