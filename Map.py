def char_range(i1, i2):
    for i in range(ord(i1), ord(i2)+1):
        yield chr(i)

map_dict = {}
default_val = 0


for i in char_range("a", "j"):
	for j in range(1, 11):
		map_dict[str(i)+str(j)] = default_val