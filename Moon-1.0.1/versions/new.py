#  Github.com/7ua  

# PACKAGES #
import random 
import time
import requests
import os
import sys
import enquiries
from colorama import Fore, Back, Style
from config import *
# PACKAGES #

# CLEAR PROMPT #
os.system("clear")
# CLEAR PROMPT #

# STARTUP #
print("Mooncord. Made by Github.com/7ua. Mooncord will now start in a second.")
time.sleep(0.9)
os.system('clear')
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']
logo = ("""

 ███▄ ▄███▓ ▒█████   ▒█████   ███▄    █  ▄████▄   ▒█████   ██▀███  ▓█████▄ 
▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
▓██    ▓██░▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌
▒██    ▒██ ▒██   ██░▒██   ██░▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
▒██▒   ░██▒░ ████▓▒░░ ████▓▒░▒██░   ▓██░▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓ 
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ 
░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░ ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░ 
       ░       ░ ░      ░ ░           ░ ░ ░          ░ ░     ░        ░    
                                        ░                           ░      

                                                  

  Made by: Github.com/7ua. Orginal repo: Github.com/7ua/Moon.
  
""")
# STARTUP #

#  LOADING SETTINGS #
if lettersOnly == True:
 a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if numbersOnly == True:
  a=['1','2','3','4','5','6','7','8','9','0']
if lnmix == True:
  a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']
#  LOADING SETTINGS #

#MAIN MENU#
print(Fore.RED + logo)
options = ['\033[31m'+'Nitro gen & checker. ', '\033[31m'+'Nitro gen (no checker) ', '\033[31m'+'invite gen (no checker) ', '\033[31m'+'Token Generator', '\033[31m'+'exit']
choice = enquiries.choose('Choose one of these options: ', options)
# MAIN MENU #

# OP 1 #
if choice == "\033[31mNitro gen & checker. ":
 while True:                              
  # CREATE CODE #
   w = random.choice(a)                                                           
   d = random.choice(a)                                                           
   e = random.choice(a)                                                           
   f = random.choice(a)                                                           
   g = random.choice(a)                                                           
   h = random.choice(a)                                                           
   i = random.choice(a)
   j = random.choice(a) 
   k = random.choice(a) 
   l = random.choice(a) 
   n = random.choice(a) 
   o = random.choice(a) 
   p = random.choice(a) 
   q = random.choice(a) 
   r = random.choice(a) 
   s = random.choice(a) 
   m = f+e+w+d+g+h+i+j+k+l+n+o+p+q+r+s    
   # CREATE CODE #
   c = 'https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'?with_application=false&with_subscription_plan=true'
    #CHECK CODE#                                                                              
   b = requests.get(c)                                                            
   if b.status_code == 404:                                                       
                                                                                  
    print(Fore.WHITE+Back.RED +'[INVAILD]'+Style.RESET_ALL+'\033[31m' + '[x]: discord.gifts/'+m+' Was invalid'+ '\033[0m')            
   if b.status_code == 429:                                                       
    print(Fore.WHITE+Back.YELLOW+"[WARNING]"+Style.RESET_ALL+"\033[1;33m"+"[-]: Rate Limited | Waiting 40 Seconds |"+"\033[0m")
    time.sleep(39.9)
        #SNIPER OPTION#                                                                           
   if b.status_code == 200:                                                       
    print('[GOOD] [+]: discord.gifts/'+m+'Is Valid!')
    if sniperOn == True:
      requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'/redeem', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
      print('Nitro redeemed!')
      if sniperOn == False:
       file = open("okcodes.txt", "w")                                              
       file.write('discord.gifts/'+m)                                               
       file.close()
       print("Code saved in 'okcodes.txt'")
       #SNIPER OPTION# 
       #CHECK CODE#  
       
       #REST OF THE OP#
if choice == "\033[31mNitro gen (no checker) ":
 os.system('python3 gen1.py')
if choice == "\033[31minvite gen (no checker) ":
 os.system('python3 invitegen.py')
if choice == "\033[31mToken Generator":
 os.system('python3 tokeng.py')
if choice == "\033[31mexit":
 sys.exit()
