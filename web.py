import requests
import os 
import  time 
import time as mm
import sys as n
import  webbrowser
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

print (\033[32m"""
░██╗░░░░░░░██╗███████╗██████╗░██████╗░░█████╗░░██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝░
░╚██╗████╗██╔╝█████╗░░██████╦╝██████╔╝███████║██║░░██╗░
░░████╔═████║░██╔══╝░░██╔══██╗██╔═══╝░██╔══██║██║░░╚██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░░░░██║░░██║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░
           \033[0;96m[+] Coded By Mr Sami Channel : t.me/TYG_YE

""")

sami =input("\033[32m[+] 𝐄𝐧𝐭𝐞𝐫 𝐔𝐫𝐥 𝐒𝐢𝐭𝐞 : ")
ye = requests.get(sami).text
yemen = open('code.html','w')
yemen.write(f'{ye}')
yemen.close()

slow('\033[32m\n\nThe file is saved with the following name code.html')
webbrowser.open("https://t.me/TYG_YE")
