import os
import curses
from curses import wrapper



from time import sleep





def clearScreen():
	os.system("cls") if os.name == 'nt' else os.system("clear")
n = 60

myString1 ="                                //////////                                      "

myString2 ="                               .//////////                                       "

myString3 ="                                  ###*                                           "

myString4 ="                            /////////////////,                                   "

myString5="                            /////////////////,                                   "

myString6="           .           ,,,,,,,,,,**###/******,                                   " 

myString7="          #(((((((#*.///////////(((((((((((((*                     ,/##(         "

myString8="               ,/#(/////#%%%///((((//////////////////////*#(((((((((((#(         "

myString9="                 ,/////////////((((/////#%%%///#%%%////////((*.                  "

myString10="                 ,/////////////((((/////#%%%///%%%%//////////                    " 

myString11="                   ((((((((((((((((//////////////////////////.                   " 

myString12="       ##################################################################(     "

myString13="       ##################################################%%%%%###########*     " 

myString14="         /##############################################%&&&&&&######%........."

myString15="..........%########################################################............"

myString16="...........*######################################################.............."

def main(stdscr):
    
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    BLACK_AND_BLUE = curses.color_pair(1)
    BLACK_AND_WHITE = curses.color_pair(2)
    BLUE_AND_WHITE = curses.color_pair(3)
    
    stdscr.addstr( myString1 , BLUE_AND_WHITE)


wrapper(main)






while n > 0:
	clearScreen()	
	print("\033[1;30;47m " + myString1[n:])
	print(myString2[n:])
	print(myString3[n:])
	print(myString4[n:])
	print(myString5[n:])
	print(myString6[n:])
	print(myString7[n:])
	print(myString8[n:])
	print(myString9[n:])
	print(myString10[n:])
	print(myString11[n:])
	print("\033[1;37;44m " + myString12[n:])
	print(myString13[n:])
	print(myString14[n:])
	print(myString15[n:])
	print(myString16[n:])
	sleep(0.1)


	n = n - 1






