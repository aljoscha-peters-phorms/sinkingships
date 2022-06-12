"""
class Ships():

	def __init__(self, schiffTypen : schiff_Typen):
		self.id = 0
		self.name = ""
		self.stellen = []
		for i in range(schiff_Typen[schiffTypen]):
			self.stellen.append(False)
		self.zeichen = ""

	def setID(self, newID):
		self.id = newID

	def getID(self):
		return self.id

	def setStellen(self, newStellen):
		self.stellen = copy.copy(newstellen)

	def getStellen(self):
		return self.stellen

	def setStelle(self, pos, value):
		self.stellen[pos] = value

	def getStelle(self, pos):
		return self.stelle[pos]

	def setZeichen(self, newValue):
		self.zeichen = newValue

	def getZeichen(self):
		return self.zeichen
"""