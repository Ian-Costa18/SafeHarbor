import ctypes, sys
from main import main
def makeAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if makeAdmin():
    main()
else:
    main()
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
