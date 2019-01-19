#!c:\users\ian\source\repos\sammythebeast\hack-wpi\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'zc.buildout==2.13.0','console_scripts','buildout'
__requires__ = 'zc.buildout==2.13.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('zc.buildout==2.13.0', 'console_scripts', 'buildout')()
    )
