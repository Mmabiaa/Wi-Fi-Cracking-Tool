from choices import choice0, choice1, choice2, choice3, choice4, choice6, choice7, choice8, choice9, choice10, choice0, choice11
from cracker import wire


# Author - Mmabiaa
# All rights observed!


def intro():

    print("""\033[1;32m
---------------------------------------------------------------------------------------
██╗    ██╗██╗███████╗██╗       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                        Author - Mmabiaa""")
    print("""
---------------------------------------------------------------------------------------
(1)Start monitor mode
(2)Stop monitor mode
(3)Scan Networks
(4)Getting Handshake(monitor mode needed)
(5)Install Wireless tools
(6)Crack Handshake with 'rockyou.txt' (Handshake needed)
(7)Crack Handshake with word list    (Handshake needed)
(8)Crack Handshake without word list (Handshake,ESSID needed)
(9)Create word list
(10)WPS Networks attacks (BSSID,monitor mode needed)
(11)Scan for WPS Networks

(0)About Me
(00)Exit
-----------------------------------------------------------------------
""")


def check_user_choice():
    print("\nEnter your choice here : !# ")
    var = int(input(""))
    if var == 1 :
        choice1()
    elif var == 2 :
        choice2()
    elif var == 3 :
        choice3()

    elif var == 4 :
        choice4()

    elif var == 5 :
        wire()

    elif var == 0 :
        choice0()

    elif var == 00:
        exit()

    elif var == 6:
        choice6()

    elif var == 7 :
        choice7

    elif var == 8 :
        choice8()


    elif var == 9 :
        choice9()

    elif var == 10:
        choice10()

    elif var == 11:
        choice11()

    else:
        print('Invalid input....Please try again later')

def main():
    intro()
    check_user_choice()

main()
