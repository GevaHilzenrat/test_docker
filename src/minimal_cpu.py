import os
import platform

print(f"Python version: {platform.python_version()}")
print(f"CPU cores (logical): {os.cpu_count()}")

import multiprocessing
print(f"CPU cores (multiprocessing): {multiprocessing.cpu_count()}")

try:
    with open("/proc/cpuinfo") as f:
        cpuinfo = f.read()
    model = [l.split(":")[1].strip() for l in cpuinfo.splitlines() if "model name" in l]
    if model:
        print(f"CPU model: {model[0]}")
except:
    print(f"CPU model: {platform.processor()}")

"""
# Example output:

Python version: 3.12.0
CPU cores (logical): 8
CPU cores (multiprocessing): 8
CPU model: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
"""