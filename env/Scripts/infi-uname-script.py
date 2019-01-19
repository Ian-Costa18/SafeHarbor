#!c:\users\ian\source\repos\sammythebeast\hack-wpi\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'infi.os-info==0.1.11','console_scripts','infi-uname'
__requires__ = 'infi.os-info==0.1.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('infi.os-info==0.1.11', 'console_scripts', 'infi-uname')()
    )
