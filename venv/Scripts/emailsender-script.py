#!C:\Users\rodrigo.galvao\PycharmProjects\FirstProgram\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'emailsender==0.1.3','console_scripts','emailsender'
__requires__ = 'emailsender==0.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('emailsender==0.1.3', 'console_scripts', 'emailsender')()
    )
