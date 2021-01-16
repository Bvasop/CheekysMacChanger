import subprocess
import optparse
import re
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

def giris():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface degistirme")
    parse.add_option("-m","--mac",dest="mac_adress",help="yeni mac")
    return parse.parse_args()

def mac(inter,mac_adres):
    subprocess.call(["ifconfig",inter,"down"])
    subprocess.call(["ifconfig",inter,"hw","ether",mac_adres])
    subprocess.call(["ifconfig",inter,"up"])

def kontrol(interface):
    ifconfig= subprocess.check_output(["ifconfig",interface])
    yMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if yMac:
        return yMac.group(0)
    else:
        return None

print(""" \n \n [ Mac Degistirme Basladi ] 
		  \   \   \   \   \   \ 
		   ######    #      #      ########## 
		  #	     #	    #     #
		 #	     ########    #     ####
		  #	     #	    #   #	  #	
		   ######    #	    #	##########	
			
""")

(userInput,arguments)=giris()
mac(userInput.interface,userInput.mac_adress)
eMac = kontrol(userInput.interface)

if eMac == userInput.mac_adress:
    print(Fore.BLUE)
    print("""			Bozkurt Farki ile Basarili  \n                           Cheeky's Hacking Group \n""")
    print(Fore.GREEN)
    print(os.system("ifconfig eth0"))
    

else:
    print("Basarisiz")