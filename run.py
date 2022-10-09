from subprocess import Popen
from win32process import DETACHED_PROCESS
pid = Popen(["venv/Scripts/python.exe", "main.py"], creationflags=DETACHED_PROCESS,
            shell=False).pid