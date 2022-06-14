import globale
import os


def char_range(i1, i2):
	#outputs range of characters
	for i in range(ord(i1), ord(i2)+1):
		yield chr(i)

def clearScreen():
	#clears terminal with terminal clear command for respective os's
	os.system("cls") if os.name == "nt" else os.system("clear")

global count
count = []

class Map():
	
	def __init__(self):
		self.map_dict = {}

	def mapDictInit(self):
		#default val is 0 for water
		default_val = "0"

		for i in char_range("a", "j"):#a to j bc map goes from a1 b1 ... i1 j1.
			for j in range(1,11):# map goes from a1 a2 to a9 a10
				self.map_dict[str(i)+str(j)] = default_val #goes through a1-10, b1-10 ... j1-10, sets val as default val

	def inMap(self, start_feld, laenge, orient):
		#gets orientation, length, starting field and checks if its in the map
		#different because vertical and horizontal calc is different
		if orient == "v":
			return int(start_feld[1]) + laenge <= 10 #return true if length + digit of starting field is smaller than 10,
													#so if the ship doesn't go out of bounds
		
		return ord(start_feld[0]) + laenge <= ord("j")#returns true if char from start field
													#+ length dont go above j which is out of bounds

	def besetzt_v(self, start_feld, laenge):
		sp = start_feld[0]#first char of start field(character)
		zl = int(start_feld[1])#second char of start field(number)
		for i in range(0, laenge):
			try:
				if self.map_dict[sp+str(zl + i)] != 0:# gives back true if any of the keys of the dict
					return False					# on start field and lenght return 0
			except KeyError:# if the key asked doesn't exist or inMap() didnt catch error, also returns true
				return False
		return True#if all fields can be placed on returns false

	def besetzt_h(self, start_feld, laenge):
		sp = start_feld[0]
		zl = start_feld[1]

		for i in range(0, laenge):
			try:				#character of start field incremented by length + number of start field
				if self.map_dict[chr(ord(sp)+i) + zl] != 0:# gives back true if any of the keys of the dict
					return False						# on start field and lenght return 0
			except KeyError:
				return False
		return True

	def schiffeSetzen(self, schiffTyp, start_feld, orient):
		if self.inMap(start_feld, globale.schiff_Typen[schiffTyp], orient) == False:
			return False # returns false if the inMap() says ship with length from dict on start field in that orient is not possible


		if orient == "v":
			if self.besetzt_v(start_feld, globale.schiff_Typen[schiffTyp]) == False:
				sp = start_feld[0]
				zl = int(start_feld[1])
				for i in range(0, globale.schiff_Typen[schiffTyp]):
					self.map_dict[sp+str(zl + i)] = globale.schiff_Codierung[schiffTyp]
				return True#same func from before but loops through and assignes (from ship dict) not compares

		elif orient == "h":
			if self.besetzt_h(start_feld, globale.schiff_Typen[schiffTyp]) == False:
				sp = start_feld[0]
				zl = start_feld[1]
				for i in range(0, globale.schiff_Typen[schiffTyp]):
					self.map_dict[chr(ord(sp)+i) + zl] = globale.schiff_Codierung[schiffTyp]
				return True#same as above but different orientation
		return False

	def changeStellen(self, stelle, zeichen):
		self.map_dict[stelle] = zeichen # change singular key values in dictionary

	def appendStellen(self, stelle, zeichen):
		self.map_dict[stelle] = str(self.map_dict[stelle]) + zeichen # apppends value to singular key vals in dict

	def printMap(self):
		#prints out map in 2d for loops
		print("\n")

		print("\tA  B  C  D  E  F  G  H  I  J\n\n")
		
		for i in range(1,11):
			print(i, end = "\t")
			for j in range(ord("a"), ord("j") + 1):
				k = str(self.map_dict[chr(j)+str(i)])
				if len(k) == 1:
					print(k, end = "  ")
				else:
					print(k, end = " ")
				if j == ord("j"):
					print("\n")
	
	def checkSunkShip(self, schiffTyp):

		#loops through list, checks if sunk and of type of ship specified#
		#in dieser schrecklichen form für debugging, sorry, geht auch mit if and...
		for i in range(1, 11):
			for j in range(ord("a"), ord("j") + 1):
				if len(str(self.map_dict[chr(j)+str(i)])) == 2:
					if self.map_dict[chr(j)+str(i)][1] == "+":
						if int(self.map_dict[chr(j)+str(i)][0]) == globale.schiff_Codierung[schiffTyp]:
							count.append(int(self.map_dict[chr(j)+str(i)][0]))
		#returns true if the list of ship parts is the same as the length of the ship, means that whole ship sunk
		#else returns false
		if len(count) == globale.schiff_Typen[schiffTyp]:
			return True, schiffTyp
		return False, schiffTyp

#for categorising different maps, currently still difficult to access from player file/main file
class ownMap(Map):
	pass

class enemyMap(Map):
	pass

######test########

"""
s1 = Map()
s1.mapDictInit()

s1.schiffeSetzen("Battleship", "a1", "h")

s1.printMap()

s1.appendStellen("a1", "+")
s1.appendStellen("b1", "+")
s1.appendStellen("c1", "+")
s1.appendStellen("d1", "+")

s1.printMap()

print(s1.checkSunkShip("Battleship"))
"""