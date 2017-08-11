from pywinauto import Application
import time
from pywinauto.keyboard import SendKeys
app = Application().start(
    'D:\\Program Files\\SiemensST\\steamapps\\common\\jnes\\jnes.exe')
app.active()
SendKeys('%{F}')
SendKeys('{R}{1}')
SendKeys('{VK_F7}')
while app.is_process_running():
    time.sleep(1)
    SendKeys('+')
    time.sleep(1)
    SendKeys('^')
    time.sleep(1)
    SendKeys('+')
    time.sleep(1)
    SendKeys('+')
