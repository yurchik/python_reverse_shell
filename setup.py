import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="puzzel",
      version="0.1",
      description="Fun computer game",
      options={'buil_exe': {'include_files': include_files}},
      executables=[Executable("client.py", base=base)])
