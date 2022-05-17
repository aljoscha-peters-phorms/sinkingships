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
		raise Exception("Außerhalb der Karte, nochmal versuchen.")

	if orient == "v":
		if besetzt_v(start_feld, globale.schiff_Typen[schiffTyp]):
			pass

print(inMap("j1", 5, "h"))