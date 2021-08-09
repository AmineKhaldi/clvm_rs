#!/usr/bin/env python3

from run_gen import run_gen, print_spend_bundle_conditions
from time import time
import sys
import glob

failed = 0

for g in glob.glob('generators/*.clvm'):
    start_time = time()
    error_code, result = run_gen(g)
    run_time = time() - start_time

    if error_code:
        output = f"FAILED: {error_code}\n"
    else:
        output = print_spend_bundle_conditions(result)
        print(f"  cost: {result.cost}")
    with open(g) as f:
        expected = f.read().split('\n', 1)[1]
        print(f"{g}")
        if expected != output:
            print(f"output:")
            print(f"\"{output}\"")
            print("expected:")
            print(f"\"{expected}\"")
            failed = 1
        print(f"  run-time: {run_time:.2f}s")
        limit = 1.5

        # temporary higher limits until this is optimized
        if "duplicate-coin-announce.clvm" in g:
            limit = 9
        elif "negative-reserve-fee.clvm" in g:
            limit = 4

        if run_time > limit:
            print("run-time exceeds limit!")
            failed = 1

sys.exit(failed)
