import time
import os


def clear():
    os.system('clear||cls')
def print_menu():

    clear()
    print('**********************************************************************************************************************************************************************')
    print('*                                                                                                                                                                    *')
    print('*                                                                                                                                                                    *')
    print('*                                                               \u001b[36;1m ███╗   ███╗███████╗███╗   ██╗██╗   ██╗\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ████╗ ████║██╔════╝████╗  ██║██║   ██║\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝\u001b[37m                                                              *')
    print('*                                                               \u001b[36;1m ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ \u001b[37m                                                              *')
    print('*                                                                                                                                                                    *')       


    print('*                                                                                                                                                                    *')
    print('*                                                                 ▄█─ ─    ░█▀▀█ ░█─── ─█▀▀█ ░█──░█                                                                  *')    
    print('*                                                                 ─█─ ▄    ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█                                                                  *') 
    print('*                                                                 ▄█▄ █    ░█─── ░█▄▄█ ░█─░█ ──░█──                                                                  *')
    print('*                                                                                                                                                                    *')
    print('*                                                                 █▀█ ─   ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█─░█ ▀▀█▀▀                                                             *')                                                                  
    print('*                                                                 ─▄▀ ▄   ░█▄▄█ ░█▀▀▄ ░█──░█ ░█─░█ ─░█──                                                             *')                                                                  
    print('*                                                                 █▄▄ █   ░█─░█ ░█▄▄█ ░█▄▄▄█ ─▀▄▄▀ ─░█──                                                             *')
    print('*                                                                                                                                                                    *')                                                        
    print('*                                                                 █▀▀█ ─   ░█▀▀▀ ▀▄░▄▀ ▀█▀ ▀▀█▀▀                                                                     *')
    print('*                                                                 ──▀▄ ▄   ░█▀▀▀ ─░█── ░█─ ─░█──                                                                     *')
    print('*                                                                 █▄▄█ █   ░█▄▄▄ ▄▀░▀▄ ▄█▄ ─░█──                                                                     *')
    print('*                                                                                                                                                                    *')       
    print('*                                                                                                                                                                    *')       
    print("**********************************************************************************************************************************************************************")


  
    option=input("Enter your choce: ")
    if option == "1":
        time.sleep(1.0)
        clear()
        from menu import print_menu1
    elif option == "2":
      print('Data Structure Algorithm TERMINAL GAME © 2022')
      print("This is about games that implement queue, stack and linked-list.") 
     
      
      time.sleep(5.0)
      
      print(print_menu())
    elif option == "3":
     exit()

print(print_menu())

