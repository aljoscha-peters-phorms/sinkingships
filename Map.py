import globale
import os


def char_range(i1, i2):
    for i in range(ord(i1), ord(i2)+1):
        yield chr(i)

def clearScreen():
	os.system("cls") if os.name == "nt" else os.system("clear")

class Map():
	
	def __init__(self):
		self.map_dict = {}

	def mapDictInit(self):
		default_val = 0

		for i in char_range("a", "j"):
			for j in range(1, 11):
				self.map_dict[str(i)+str(j)] = default_val

	def inMap(self, start_feld, laenge, orient):
		if orient == "v":
			return int(start_feld[1]) + laenge <= 10
		
		return ord(start_feld[0]) + laenge <= ord("j")

	def besetzt_v(self, start_feld, laenge):
		sp = start_feld[0]
		zl = int(start_feld[1])
		for i in range(0, laenge):
			if self.map_dict[sp+str(zl + i)] != 0:
				return True
		return False

	def besetzt_h(self, start_feld, laenge):
		sp = start_feld[0]
		zl = start_feld[1]

		for i in range(0, laenge):
			if self.map_dict[chr(ord(sp)+i) + zl] != 0:
				return True
		return False

	def schiffeSetzen(self, schiffTyp, start_feld, orient):
		if self.inMap(start_feld, globale.schiff_Typen[schiffTyp], orient) == False:
			return False

		if orient == "v":
			if self.besetzt_v(start_feld, globale.schiff_Typen[schiffTyp]) == False:
				sp = start_feld[0]
				zl = int(start_feld[1])
				for i in range(0, globale.schiff_Typen[schiffTyp]):
					self.map_dict[sp+str(zl + i)] = globale.schiff_Codierung[schiffTyp]
				return True

		if orient == "h":
			if self.besetzt_h(start_feld, globale.schiff_Typen[schiffTyp]) == False:
				sp = start_feld[0]
				zl = start_feld[1]
				for i in range(0, globale.schiff_Typen[schiffTyp]):
					self.map_dict[chr(ord(sp)+i) + zl] = globale.schiff_Codierung[schiffTyp]
				return True
		
		return False

	def changeStellen(self, stelle, zeichen):
		self.map_dict[stelle] = zeichen

	def printMap(self):
		
		print("\tA B C D E F G H I J\n\n")
		
		for i in range(1,11):
			
			print(i, end = "\t")
			for j in range(ord("a"), ord("j") + 1):
				print(self.map_dict[chr(j)+str(i)], end = " ")
				if j == ord("j"):
					print("\n")

class ownMap(Map):
	pass

class enemyMap(Map):
	pass

"""
s1 = ownMap()
s1.mapDictInit()


s1.printMap()

s1.schiffeSetzen("Fregatte", "a3", "h")
s1.schiffeSetzen("Destroyer", "g2", "v")
s1.schiffeSetzen("Carrier", "b8", "h")
print("\n")
s1.printMap()

s1.changeStellen("a1", "+")
s1.changeStellen("j10", "-")
s1.printMap()
"""