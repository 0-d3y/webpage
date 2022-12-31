import requests
import os 
import  time 
import time as mm
import sys as n
import  webbrowser
import telebot
os.system('clear')
def slow(M):
for c in M + '\n':
n.stdout.write(c)
n.stdout.flush()
mm.sleep(0.04)



#============== Color ==========
la7mar  =  '\033[91m' 
lazra9  =  '\033[94m' 
la5dhar =  '\033[92m' 
movv    =  '\033[95m' 
lasfar  =  '\033[93m' 
ramadi  =  '\033[90m' 
blid    =  '\033[1m' 
star    =  '\033[4m' 
bigas   =  '\033[07m' 
bigbbs  =  '\033[27m' 
hell    =  '\033[05m' 
saker   =  '\033[25m' 
labyadh =  '\033[00m' 
red   = '\033[31m'
#============== Color ========

print ("""
░██╗░░░░░░░██╗███████╗██████╗░██████╗░░█████╗░░██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝░
░╚██╗████╗██╔╝█████╗░░██████╦╝██████╔╝███████║██║░░██╗░
░░████╔═████║░██╔══╝░░██╔══██╗██╔═══╝░██╔══██║██║░░╚██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░░░░██║░░██║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░
           \033[0;96m[+] Coded By Mr Sami Channel : t.me/TYG_YE

""")
webbrowser.open("https://t.me/TYG_YE")
try:
sami =input("\033[32m[+] 𝐄𝐧𝐭𝐞𝐫 𝐔𝐫𝐥 𝐒𝐢𝐭𝐞 : ")
folder= input("\033[32m[+] Enter Name Folder : ")
os.mkdir(f"{folder}")
css = requests.get(sami+"/style.css").text
yemen = open(f'{folder}/style.css','w')
yemen.write(f'{css}')
yemen.close()
html = requests.get(sami).text
yemen = open(f'{folder}/code.html','w')
yemen.write(f'{html}')
yemen.close()

slow('\033[32m\n\nThe file is saved with the following name code.html')

except:
slow(f'\n\n[-]The file name you entered is already in use. Give me a new file name so I can create it for you')
slect=input("\033[0;96m\n\n[-] To exit the tool, press (x), to restart the tool, press the letter (y) ? ")
if slect == "y":
os.system("python web.py")
else:
os.system("exit")
