# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:32:24 2020

@author: Ham

The Python Standard Library: Coroutines and Tasks

Trying out sample codes provided in there to understand better.

"""

import sys
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')}", sys._getframe(0).f_code.co_name + '():',
          what)

# Source: Real Python
async def async_sleep(tag, delay=1):
    print(f"{time.strftime('%X')}",
          f"{sys._getframe(0).f_code.co_name}({str(tag)}, {str(delay)}):",
          "before")
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')}",
          f"{sys._getframe(0).f_code.co_name}({str(tag)}, {str(delay)}):",
          "after")

async def main():
    print(f"{time.strftime('%X')}", sys._getframe(0).f_code.co_name + '():',
          "starting ...")

    await say_after(97 - 94, 'hello')
    print("after 1st await")
    await say_after(134 - 133, 'world')
    print("and after 2nd await")
    await say_after(102 - 100, 'again')

    await asyncio.gather(async_sleep(1, 3), async_sleep(2, 2), async_sleep(3))

    print(f"{time.strftime('%X')}", sys._getframe(0).f_code.co_name + '():',
          "... completed")

if __name__ == "__main__X":
    # CANNOT simply run within Spyder/Jupyter (by clicking a Run button)!
    # Because the IPython kernel is already running an event loop.
    # So to run within Spyder/Jupyter, must do:    !run async_await.py
    # Observations:
    #   1. Long delay till output appears, ~46-76secs
    #   2. Output are shown altogether (i.e. no pause) even if long delays were
    #      specified in-between. However, timestamps show correct delays.
    #      Probably all lines were buffered together by "!run"
    #   3. So the overall delay seems to be the sum of the start-up delay,
    #      plus all await.
    # --------------
    #   That was then, here's the proper way to run from within Spyder/Jupyter:
    #   4. Click the Run button. It'll fail but IPython has the latest defs.
    #      (Also, after making changes to the source, need to Run again.)
    #   5. IPython prompt:    await  main()
    #   6. It'll run immediately (i.e. *NO* delay for 1st output)
    #   7. Subsequent lines appear 1-by-1 after the correct delays;
    #      i.e. yup, visible pauses in-between

    print(f"{time.strftime('%X')}", f"{__file__}:", "BEGIN")

    asyncio.run(main())
    #await main()

    print(f"{time.strftime('%X')}", f"{__file__}:", "END")
