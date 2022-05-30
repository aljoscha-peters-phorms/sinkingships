"""
import curses
import time
from curses import wrapper

def main(stdscr):
    # Clear screen
    
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    RED_AND_GREEN = curses.color_pair(2)
    blue_and_white = curses.color_pair(3)

    counter_win = curses.newwin(1,20,10,10)
    
    for i in range(100):
        counter_win.clear()
        color = blue_and_white
        if i % 2 == 0:
            color = BLUE_AND_YELLOW
        counter_win.addstr(f'Count: {i}', color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()

<<<<<<< HEAD
wrapper(main)
"""

n = 0

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

myString14="         /##############################################%&&&&&&######%         "

myString15="          %########################################################.           "

myString16="          *######################################################.             "
while n == -50:
	print(myString1[:n])
	print(myString2[:n])
	print(myString3[:n])
	print(myString4[:n])
	print(myString5[:n])
	print(myString6[:n])
	print(myString7[:n])
	print(myString8[:n])
	print(myString9[:n])
	print(myString10[:n])
	print(myString11[:n])
	print(myString12[:n])
	print(myString13[:n])
	print(myString14[:n])
	print(myString15[:n])
	print(myString16[:n])
	n = n - 1








=======
wrapper(main)
>>>>>>> 3848c836f379d180c07da9a0dfc2e83eb1ba1d4e
