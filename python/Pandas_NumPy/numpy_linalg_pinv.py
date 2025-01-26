#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:00:17 2025

@author: Gregory Guyomarc'h from Apple Slack #help-python
import os

n = 8
nthreads_env_variables = [
    # numpy backends:
    "MKL_NUM_THREADS",  # MKL
    "NUMEXPR_NUM_THREADS",  # NumExpr
    "OMP_NUM_THREADS",  # OpenMP
    "OPENBLAS_NUM_THREADS",  # OpenBLAS
    "VECLIB_MAXIMUM_THREADS",  # vecLib/Accelerate
]
for key in nthreads_env_variables:
    os.environ[key] = str(n)

Setting $OMP_NUM_THREADS does affect runtime
Whereas $OPENBLAS_NUM_THREADS seems NOT to affect runtime!
When not specified, runtime seems to be the same as OMP_NUM_THREADS=1???

Then just call:
❯ OMP_NUM_THREADS=8 python cputest.py
seconds=5.8874
❯ OMP_NUM_THREADS=1 python cputest.py
seconds=20.1227

=====

Ham Nguyen's favorite one-liner:

$ /usr/bin/time /bin/zsh -c 'OMP_NUM_THREADS=8 python -c "import numpy; numpy.linalg.pinv(numpy.random.random((4_000, 4_000)))"'
       11.00 real        54.06 user         1.94 sys

$ /usr/bin/time /bin/zsh -c 'OMP_NUM_THREADS=1 python -c "import numpy; numpy.linalg.pinv(numpy.random.random((4_000, 4_000)))"'
       26.33 real        25.73 user         0.58 sys

$ /usr/bin/time /bin/zsh -c 'OMP_NUM_THREADS=16 python -c "import numpy; numpy.linalg.pinv(numpy.random.random((4_000, 4_000)))"'
       31.79 real       312.83 user         6.25 sys
$ /usr/bin/time /bin/zsh -c 'OMP_NUM_THREADS=10 python -c "import numpy; numpy.linalg.pinv(numpy.random.random((4_000, 4_000)))"'
       11.85 real        68.84 user         2.90 sys

$ time python -c "import numpy; numpy.linalg.pinv(numpy.random.random((8_000, 8_000)))"

real	1m23.274s
user	10m42.727s
sys	0m10.746s

$ time /bin/zsh -c 'OMP_NUM_THREADS=8 python -c "import numpy; numpy.linalg.pinv(numpy.random.random((8_000, 8_000)))"'

real	1m10.541s
user	7m6.280s
sys	0m8.187s
"""

import numpy
import datetime

m = numpy.random.random((4_000, 4_000))
start = datetime.datetime.now()
numpy.linalg.pinv(m)
end = datetime.datetime.now()
seconds = (end - start).total_seconds()
print(f"{seconds=:.4f}")
