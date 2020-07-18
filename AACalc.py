from AACalcGuns import *  
from AACalcFuncs import *
from AACalcClasses import *

'''
Ship data guide:
s# = Ship(name, reload, aaStat, slotEff, aaSkill, relSkil)
s# = Ship(string, int,   int,    float,    int,        int)
'''
# Edit these to match your fleet (following above format)
formationBonus = .2 # .2 for diamond formation, 0 for others
minimumRange = None

'''
# My W13 Boss Fleet
s1 = Ship("Sandy", 210, 734, 1.85, 0.75, 0)
s2 = Ship("Portland", 170, 305, 1.35, 0.5, 0)
s3 = Ship("Roon", 166, 278, 1.05, 0.5, 0)
s4 = Ship("Nagato", 146, 227, 1, 0.5, 0)

# Make sure each item is in this list:
shipList = [s1, s2, s3, s4]
'''
'''
# My W13 Mob Fleet
shipList = [
    Ship("Ning Hai", 187, 449, 1.35, 0.07, 0.15),
    Ship("Yat Sen", 182, 492, .80, 0.07, 0.15),
    Ship("Baltimore", 181, 302, 1.35, 0.07, 0.15),
    Ship("Alabama", 154, 478, 1, 0.07, 0.15),
    Ship("Akashi G1", 181, 250, 1, 0.07, 0.15),
    Ship("Akashi G2", 181, 250, 1, 0.07, 0.15)
]
'''
'''
shipList = [
    #Ship("Ning Hai", 187, 449, 1.35, 0.0, 0.15),
    #Ship("Yat Sen", 182, 492, .80, 0.0, 0.15),
    #Ship("Baltimore", 181, 302, 1.35, 0.07, 0.15),
    Ship("Yuubari", 194, 319+145, 1.25, 0, 0),
    Ship("Mogami", 178, 223+145, 1.05, 0, 0),
    Ship("Yukikaze", 223, 161+45+30, .75, 0, 0),
    Ship("Alabama", 154, 478, 1, 0.0, 0.15),
    Ship("Akashi G1", 181, 250, 1, 0.0, 0.15),
    Ship("Akashi G2", 181, 250, 1, 0.0, 0.15)
]

# Make sure each item is in this list:
#shipList = [s1, s2, s3, s4, s5, s6]
'''
# Best AA Ships comparison
shipList = [
    #Ship("Cheshire Gun 1", 156, 409  + 200 + 45 + 45, 1.65, .15, 0),
    #Ship("Cheshire Gun 2", 156, 409  + 200 + 45 + 45, 1.65, .15, 0),
    #Ship("Sandy", 210, 559 + 200 + 45, 1.85, 0.75, 0)
    Ship("Seattle Gun 1", 156, 365 + 200 + 45 + 45, 1.3, .15, .2),
    Ship("Seattle Gun 2", 156, 365 + 200 + 45 + 45, 1.3, .15, .2)
]

# DONT EDIT PAST THIS


# Populates initial gun guesses
currentGunList = []
for i in range(len(shipList)):
    currentGunList.append(gunList[0])

# sets up data for recursive calculation call
numLoops = len(currentGunList)
startLoop = 0
startDPS = 0

# Creates an object to keep track of the loadout stats
fleetLoadout = Fleet(currentGunList, startDPS)

# Peforms calculation
recursiveCalculate(currentGunList, gunList, shipList, formationBonus, numLoops, startLoop, fleetLoadout, minimumRange)
radius = calculateRadius(fleetLoadout.getAllGuns())

# Output section
print("Max fleet AA DPS: ", round(fleetLoadout.getDPS(), 2))
print("The fleet AA radius is: ", round(radius, 2) , "units")

for i in range(len(shipList)):
    print("Ship: ", shipList[i].getName() , "Best Equipment: ", fleetLoadout.getAllGuns()[i].getName())




#TODO: Find way to store and compare multiple comps?
#TODO: Create GUI
#TODO: Create ship database with stats