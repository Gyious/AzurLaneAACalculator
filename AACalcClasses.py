import copy
'''
A lot of things in this file are unused, but potentially useful.
A few things might be unoptimal or not used/usable (didnt update them) - but there should be few things like this
'''


class Ship:
    def __init__(self, name, reload, aaStat, slotEff, aaSkil, relSkil):
        self.name = name
        self.reload = reload
        self.aaStat = aaStat
        self.slotEff = slotEff
        self.aaSkill = aaSkil
        self.relSkill = relSkil

    # Getters
    def getName(self):
        return self.name
    
    def getReload(self):
        return self.reload

    def getAAStat(self):
        return self.aaStat

    def getSlotEff(self):
        return self.slotEff

    def getAASkill(self):
        return self.aaSkill

    def getRelSkill(self):
        return self.relSkill

    # Setters
    def setName(self, newItem):
        self.name = newItem
        return
    
    def setReload(self, newItem):
        self.reloadname = newItem
        return

    def setAAStat(self, newItem):
        self.aaStat = newItem
        return

    def setSlotEff(self, newItem):
        self.slotEff = newItem
        return

    def setAASkill(self, newItem):
        self.aaSkill = newItem
        return

    def setRelSkill(newItem):
        self.relSkill = newItem
        return

class Gun:
    def __init__(self, name, quantity, damage, fireRate, gunRange):
        self.name = name
        self.quantity = quantity
        self.damage = damage
        self.fireRate = fireRate
        self.gunRange = gunRange


    # Getters
    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity
    
    def getDamage(self):
        return self.damage

    def getFireRate(self):
        return self.fireRate

    def getRange(self):
        return self.gunRange

    # Setters
    def setName(self, newItem):
        self.name = newItem
        return
    
    def setName(self, newItem):
        self.name = newItem
        return
    
    def setQuantity(self, newItem):
        self.quantity = newItem
        return

    def setDamage(self, newItem):
        self.fireRate = newItem
        return

    def setRange(self, newItem):
        self.gunRange = newItem
        return

    # other functions
    def decriment(self):
        self.quantity -= 1
        return

    def increment(self):
        self.quantity += 1
        return

    def isOwned(self):
        if(self.quantity > 0):
            return True
        else:
            return False


class Fleet:
    def __init__ (self, guns, dps):
        self.guns = guns
        self.dps = dps
        self.flag = False

    def getAllGuns(self):
        return self.guns

    def getSingleGun(self, index):
        return self.guns[index]
    
    def getDPS(self):
        return self.dps

    def checkFlag(self):
        return self.flag

    def setAllGuns(self, newGunList):
        self.guns = copy.deepcopy(newGunList)
        return

    def setSingleGun(self, index, newGun):
        self.guns[index] = newGuns
        return

    def setDPS(self, newDPS):
        self.dps = newDPS
        return
    
    def setFlag(self):
        self.flag = True
        return