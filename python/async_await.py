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

async def main():
    print(f"{time.strftime('%X')}", sys._getframe(0).f_code.co_name + '():',
          "starting ...")

    await say_after(7, 'hello')
    await say_after(10, 'world')

    print(f"{time.strftime('%X')}", sys._getframe(0).f_code.co_name + '():',
          "... completed")

if __name__ == "__main__":
    # CANNOT simply run within Spyder/Jupyter (by clicking a Run button)!
    # Because the IPython kernel is already running an event loop.
    # So to run within Spyder/Jupyter, must do:    !run async_await.py
    # (The 1st run starts really slow, but subsequent re-runs start faster.)
    asyncio.run(main())
