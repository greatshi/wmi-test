from distutils.core import setup
import py2exe


options = {"py2exe" :
    {



    "dll_excludes": [ "USER32.dll", "SHELL32.dll", "ADVAPI32.dll", "WS2_32.dll", "GDI32.dll", "KERNEL32.dll",
                      "OLEAUT32.dll", "VERSION.dll", "ole32.dll", "WINSPOOL.DRV"] }}

setup(
    options=options,
    console=['test02.py'])