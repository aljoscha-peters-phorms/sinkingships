#menu.py
import Intro

def menu():
	Intro.asciiIntro()
	
	print("welcome to Sinking Ships")
	input1 = input("Type OK if you want to start playing\n" )



	if input1 == "OK":
		print("have fun")
		print("Regeln: Ihr spielt immer abwechselnd, merkt euch wer dran ist! \n ")
	else:
		print("ok bye")