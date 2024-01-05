import platform
import os


def cd_then_exec(dir, windows_cmd, else_cmd):
    if "Windows" in platform.system():
        return os.system("cd /D %s && %s" % (dir, windows_cmd))
    else:
        return os.system("cd %s && %s" % (dir, else_cmd))
