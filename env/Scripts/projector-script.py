#!c:\users\ian\source\repos\sammythebeast\hack-wpi\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'infi.projector==1.0.7','console_scripts','projector'
__requires__ = 'infi.projector==1.0.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('infi.projector==1.0.7', 'console_scripts', 'projector')()
    )
