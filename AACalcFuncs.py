import math

# Needs: weapon reload, ship reload, skill bonus
def calculateReload(weaponReload, shipReload, skillMod):

    inner = 200/((shipReload * (1 + skillMod)) + 100)
    reload = weaponReload * math.sqrt(inner)

    return reload

# Needs: Equipment damage, slot efficiency, AA stat, formation bonus, skill bonus
def calculateGunDamage(equipDamage, efficiency, aaStat, skillMod, formMod):

    right = (100 + aaStat * (1 + formMod + skillMod))/100
    left = equipDamage * efficiency
    damage = left * right

    return damage

# Needs: Each gun damage
def calculateFinalDamage(gunList, shipList, formMod):

    finalDamage = 0
    for i in range(len(shipList)):
        finalDamage += calculateGunDamage(gunList[i].getDamage(), shipList[i].getSlotEff(), shipList[i].getAAStat(), shipList[i].getAASkill(), formMod)

    return finalDamage

# Needs: a list
def sumList(inList):

    runningTotal = 0
    
    for i in inList:
        runningTotal += i

    return runningTotal

# Needs: sum of reloads, number of guns
def calculateFireRate(currentGunList, shipList):

    avgReload = 0
    for i in range(len(shipList)):
        avgReload += calculateReload(currentGunList[i].getFireRate(), shipList[i].getReload(), shipList[i].getRelSkill())

    avgReload = avgReload/len(shipList)

    return avgReload + 0.5

# Needs: sum of radii, number of guns
def calculateRadius(loadout):

    totalRange = 0
    for gun in loadout:
        totalRange += gun.getRange()
    
    averageRange = totalRange / len(loadout)
    finalRange = averageRange + 0.5

    return finalRange

# Needs: totalDamage, finalFireRate
def calculateDPS(currentGunList, shipList, formMod):

    finalDamage = calculateFinalDamage(currentGunList, shipList, formMod)
    RoF = calculateFireRate(currentGunList, shipList)
    finalDPS = finalDamage/RoF

    return finalDPS

# Needs: number of loops, calcDPS reqs
def recursiveCalculate(currentGunList, gunList, shipList, formMod, numLoops, currentLoop, fleet, minimumRange):
    if(currentLoop < numLoops):
        for gun in gunList:
            if(gun.isOwned()):
                gun.decriment()
                currentGunList[currentLoop] = gun
                recursiveCalculate(currentGunList, gunList, shipList, formMod, numLoops, currentLoop + 1, fleet, minimumRange)
                gun.increment()
            else:
                pass 
    else:
        DPS = calculateDPS(currentGunList, shipList, formMod)
        radius = math.floor(calculateRadius(fleet.getAllGuns()))

        if(DPS > fleet.getDPS()):
            if(minimumRange):
                if(radius > minimumRange):
                    fleet.setFlag()
                    fleet.setDPS(DPS)
                    fleet.setAllGuns(currentGunList)
            else:
                fleet.setFlag()
                fleet.setDPS(DPS)
                fleet.setAllGuns(currentGunList)