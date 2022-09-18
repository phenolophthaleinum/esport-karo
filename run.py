import os
import pathlib


scripts = [str(x) for x in list(pathlib.Path('.').glob("esport_*.py"))]
for script in scripts:
    os.system(f'python {script}')