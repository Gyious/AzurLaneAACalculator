from AACalcGuns import *  
from AACalcFuncs import *
from AACalcClasses import *

# Edit this based on formation (.2 for diamond, 0 otherwise)
formationBonus = .2 # .2 for diamond formation, 0 for others
minimumRange = None # Always leave this as None (unimplemented)

'''
Ship data guide:
Ship(name, reload, aaStat, slotEff, aaSkill, relSkil)
Ship(string, int,   int,    float,   float,   float)

Most modifiers are input as listed values with the decimal moved to the left 2 places (100% -> 1.0, 130% -> 1.3)
Slot efficiency default value should be 1, skill modifiers default value should be 0
'''
# Example inputs:
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
# Best AA Ships comparison ships (only uncommented 1 at a time for comparing
# (or 2 for ships with double guns)
shipList = [
    #Ship("Cheshire Gun 1", 156, 409  + 200 + 45 + 45, 1.65, .15, 0),
    #Ship("Cheshire Gun 2", 156, 409  + 200 + 45 + 45, 1.65, .15, 0),
    #Ship("Sandy", 210, 559 + 200 + 45, 1.85, 0.75, 0)
    Ship("Seattle Gun 1", 156, 365 + 200 + 45 + 45, 1.3, .15, .2),
    Ship("Seattle Gun 2", 156, 365 + 200 + 45 + 45, 1.3, .15, .2)
]
'''
# Current inputs (edit this):
shipList = [
    Ship("Sandy", 210, 559 + 200 + 45, 1.85, 0.75, 0)
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
#TODO: Dont do other todos and instead port to google sheets