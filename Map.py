import globale

map_dict = {}

def char_range(i1, i2):
    for i in range(ord(i1), ord(i2)+1):
        yield chr(i)

def mapDictInit():
	default_val = 0

	for i in char_range("a", "j"):
		for j in range(1, 11):
			map_dict[str(i)+str(j)] = default_val

def inMap(start_feld, laenge, orient):
	if orient == "v":
		return int(start_feld[1]) + laenge <= 10
	
	return ord(start_feld[0]) + laenge <= ord("j")

def besetzt_v(start_feld, laenge):
	sp = start_feld[0]
	zl = int(start_feld[1])
	for i in range(0, laenge):
		if map_dict[sp+str(zl + i)] != 0:
			return True
	return False

def besetzt_h(start_feld, laenge):
	sp = start_feld[0]
	zl = start_feld[1]

	for i in range(0, laenge):
		if map_dict[chr(ord(sp)+i) + zl] != 0:
			return True
	return False

def schiffeSetzen(schiffTyp, start_feld, orient):
	if inMap(start_feld, globale.schiff_Typen[schiffTyp], orient) == False:
		return False

	if orient == "v":
		if besetzt_v(start_feld, globale.schiff_Typen[schiffTyp]) == False:
			sp = start_feld[0]
			zl = int(start_feld[1])
			for i in range(0, globale.schiff_Typen[schiffTyp]):
				map_dict[sp+str(zl + i)] = globale.schiff_Codierung[schiffTyp]
			return True

	if orient == "h":
		if besetzt_h(start_feld, globale.schiff_Typen[schiffTyp]) == False:
			sp = start_feld[0]
			zl = start_feld[1]
			for i in range(0, globale.schiff_Typen[schiffTyp]):
				map_dict[chr(ord(sp)+i) + zl] = globale.schiff_Codierung[schiffTyp]
			return True
	
	return False

def printMap():
	
	for i in range(1,11):
		for j in range(ord("a"), ord("j") + 1):
			print(map_dict[chr(j)+str(i)], end = " ")	


print(ord("a"), ord("j"))

mapDictInit()


printMap()

schiffeSetzen("Fregatte", "a3", "h")
schiffeSetzen("Destroyer", "g2", "v")
schiffeSetzen("Carrier", "b8", "h")

printMap()