#!/usr/bin/python
# -*- coding:utf-8 -*-

from random import shuffle
import datetime, time
import os, sys
try:
	import argparse
except:
	print "$ pip2 install argparse"



def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() 
        time.sleep(8./90)


def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)

def Animation(String, color):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + color + String)
        sys.stdout.flush()
    print('')

parser = argparse.ArgumentParser(description='Shuffle Modify Mac Adress and Internal IP')
parser.add_argument('-i','--interface', action='store',help='--interface enp3s0 or "ifconfig/ipconfig" to discover its network interface.')
args = parser.parse_args()

class Lab_Collors():
    vermelho = '\033[31m'
    verde = '\033[32m'
    azul = '\033[34m'
    ciano = '\033[36m'
    purple = '\033[35m'
    amarelo = '\033[33m'
    preto = '\033[30m'
    branco = '\033[37m'
    Verde_claro = '\033[39m'
    original = '\033[0;0m'

os.system('clear')
today = datetime.datetime.today()
t = today.strftime("[%H:%M:%S] - ")

class Lab_Banners():
	MacBanner = '''
                               łαbørαŧøriø Ŧαηŧαรмα

 .d8888b. 888              .d888 .d888888        888b     d888                
d88P  Y88b888             d88P" d88P" 888        8888b   d8888                
Y88b.     888             888   888   888        88888b.d88888                
 "Y888b.  88888b. 888  888888888888888888 .d88b. 888Y88888P888 8888b.  .d8888b
    "Y88b.888 "88b888  888888   888   888d8P  Y8b888 Y888P 888    "88bd88P"   
      "888888  888888  888888   888   88888888888888  Y8P  888.d888888888     
Y88b  d88P888  888Y88b 888888   888   888Y8b.    888   "   888888  888Y88b.   
 "Y8888P" 888  888 "Y88888888   888   888 "Y8888 888       888"Y888888 "Y8888P'''



class Macs_Adress():
	Mac_list = ['00:18:72:2e:7c:b5',
				'4A:1B:00:4F:0B:93',
				'00:E0:4C:4D:83:19',
				'00:E0:4C:73:9F:9F',
				'00:E0:4C:31:59:B9',
				'00:E0:4C:6E:71:8A',
				'00:E0:4C:06:78:AB',
				'00:E0:4C:03:3F:41',
				'00:E0:4C:73:55:0C',
				'00:E0:4C:13:B2:BC',
				'00:E0:4C:43:7D:0C',
				'00:E0:4C:01:18:FD',
				'00:E0:4C:77:EE:13',
				'00:E0:4C:6D:27:C7',
				'00:E0:4C:5C:A8:F5']
shuffle(Macs_Adress.Mac_list)
shuffle(Macs_Adress.Mac_list)

temp = 2

def ShuffleMac(Interface, Mac):
	print Lab_Collors.purple+Lab_Banners.MacBanner
	fastprint(Lab_Collors.verde+"\n\t Coded By : "+Lab_Collors.azul+"łuŧЋ1єr"+Lab_Collors.vermelho+"\t Telegram : "+Lab_Collors.branco+"@DreadPirateRobertt")
	print ''
	try:
		for i in range(temp):
			os.system("ifconfig {} down".format(Interface))
			os.system("ifconfig {} hw ether {}".format(Interface, Mac))
			os.system("ifconfig {} up".format(Interface))
			os.system("killall nm-applet && nm-applet & exit")
			time.sleep(4)
		Animation('Mac Address Modify..', Lab_Collors.azul)
		print ''
		slowprint(Lab_Collors.amarelo+'[*] Our New Mac is {}'.format(Lab_Collors.ciano+Mac))
		print ''
		raw_input(Lab_Collors.vermelho+t+Lab_Collors.azul+'Press Any Key to exit!')
		print ''
	except Exception as e:
		print 'error as %e' % e
		sys.exit(1)


if __name__ == '__main__':
	interface = args.interface
	if not args.interface:
		os.system('clear')
		print Lab_Collors.purple+Lab_Banners.MacBanner
		print ''
		print Lab_Collors.ciano+"[*] Usage: \n"
		print Lab_Collors.branco+"ShuffleMac.py --interface enps0"
		print Lab_Collors.branco+"ShuffleMac.py -i wlan0"
		print ''
		exit()
	else:
		ShuffleMac(interface, Macs_Adress.Mac_list[4])
