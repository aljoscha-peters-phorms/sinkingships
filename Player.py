from Map import ownMap, enemyMap, Map
import globale

class Player():
   
    def __init__(self):
        self.score = 0
        self.name = ""
        self.ShipPlacements = []
        self.ownMap = ownMap()
        self.enemyMap = enemyMap()
    
    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setOwnMap(self):
        self.ownMap.mapDictInit()
    
    def getOwnMap(self):
        self.ownMap.printMap()
    
    def setEnemyMap(self):
        self.enemyMap.mapDictInit()
    
    def getEnemyMap(self):
        self.enemyMap.printMap()
    
    def askShipPlacement(self):
        goodPlacement = False
        self.ownMap.printMap()

        while not goodPlacement:    
            for i, j in globale.schiff_Typen.items():
                placementCoord = input(f'Wo willst du {i} (Länge: {j}) setzen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: a5)')
                placementOrient = input(f'Wie willst du {i} (Länge: {j}) setzen: (Antwortformat (v: vertikal, h: horizontal)): bsp. v')
                placement = (i, placementCoord, placementOrient)
                self.ShipPlacements.append(placement)
            
            if not self.checkShipmentPlacement():
                goodPlacement = False
            else:
                goodPlacement = True

    def checkShipPlacement(self):
        
        for i in self.ShipPlacements:
            if i[2] == "v":
                if Map.besetzt_v(i[1], globale.schiff_Typen[i[0]]): #besetzt returns True if besetzt
                    return False
            if i[2] == "h":
                if Map.besetzt_h(i[1], globale.schiff_Typen[i[0]]):
                    return False
            else:#incorrect orientation input in askShipPlacement func
                return False    
        return True


p1 = Player()
p1.setOwnMap()
p2 = Player()
p2.setOwnMap()

p1.askShipPlacement()
print(p1.ShipPlacements)