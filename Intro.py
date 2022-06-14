import os
import curses
from curses import wrapper
from time import sleep
from playsound import playsound

def clearScreen():
	os.system("cls") if os.name == 'nt' else os.system("clear")

def asciiIntro():
	
	n = 60
	m = 60

	
	myString1 ="                                //////////                                     "

	myString2 ="                               .//////////                                     "

	myString3 ="                                  ###*                                         "

	myString4 ="                            /////////////////,                                 "

	myString5="                            /////////////////,                                 "

	myString6="           .           ,,,,,,,,,,**###/******,                                 " 

	myString7="          #(((((((#*.///////////(((((((((((((*                     ,/##(       "

	myString8="               ,/#(/////#%%%///((((//////////////////////*#(((((((((((#(       "

	myString9="                 ,/////////////((((/////#%%%///#%%%////////((*.                "

	myString10="                 ,/////////////((((/////#%%%///%%%%//////////                  " 

	myString11="                   ((((((((((((((((//////////////////////////.                 " 

	myString12="       ##################################################################(     "

	myString13="       ##################################################%%%%%###########*     " 

	myString14="         /##############################################%&&&&&&######%........."

	myString15="..........%########################################################............"

	myString16="...........*######################################################............."


	Header1="              _       _    _                   _     _                          "
	Header2="          ___(_)_ __ | | _(_)_ __   __ _   ___| |__ (_)_ __  ___                "

	Header3="         / __| | '_ \| |/ / | '_ \ / _` | / __| '_ \| | '_ \/ __|               "

	Header4="         \__ \ | | | |   <| | | | | (_| | \__ \ | | | | |_) \__ \               "
	Header5="         |___/_|_| |_|_|\_\_|_| |_|\__, | |___/_| |_|_| .__/|___/               "
	Header6="                                   |___/              |_|                       " 
	playsound('warship-sound.mp3')
	while n > 0:
		clearScreen()	
		print("\033[1;30;47m " + myString1[n:])
		print("\033[1;30;47m " +myString2[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString3[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString4[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString5[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString6[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString7[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString8[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString9[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString10[n:]+"\033[0;0m")
		print("\033[1;30;47m " +myString11[n:]+"\033[0;0m")
		print("\033[1;37;44m " + myString12[n:]+"\033[0;0m")
		print("\033[1;37;44m " +myString13[n:]+"\033[0;0m")
		print("\033[1;37;44m " +myString14[n:]+"\033[0;0m")
		print("\033[1;37;44m " +myString15[n:]+"\033[0;0m")
		print("\033[1;37;44m " +myString16[n:]+"\033[0;0m")
		sleep(0.1)

		n = n - 1

	while m > 0:
		clearScreen()	
		print("\033[1;30;47m " + myString1[:])
		print("\033[1;30;47m " +myString2[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString3[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString4[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString5[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString6[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString7[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString8[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString9[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString10[:]+"\033[0;0m")
		print("\033[1;30;47m " +myString11[:]+"\033[0;0m")
		print("\033[1;37;44m " + myString12[:]+"\033[0;0m")
		print("\033[1;37;44m " +myString13[:]+"\033[0;0m")
		print("\033[1;37;44m " +myString14[:]+"\033[0;0m")
		print("\033[1;37;44m " +myString15[:]+"\033[0;0m")
		print("\033[1;37;44m " +myString16[:]+"\033[0;0m")
		print("\033[1;37;44m " + Header1[m:]+"\033[0;0m")
		print("\033[1;37;44m " + Header2[m:]+"\033[0;0m")
		print("\033[1;37;44m " + Header3[m:]+"\033[0;0m")
		print("\033[1;37;44m " + Header4[m:]+"\033[0;0m")
		print("\033[1;37;44m " + Header5[m:]+"\033[0;0m")
		print("\033[1;37;44m " + Header6[m:]+"\033[0;0m")
		sleep(0.1)
		m = m - 1
	playsound('warship-sound.mp3')

asciiIntro()
