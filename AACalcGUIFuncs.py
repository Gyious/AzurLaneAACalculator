import tkinter as tk
from AACalcGuns import *  
from AACalcFuncs import *
from AACalcClasses import *

formMod = 0

formations = {
    "Select Formation": 0,
    "Line Ahead      ": 0,
    "Double Line     ": 0,
    "Diamond         ": 0.2
}

# Executes and sets formMod whenever dropdown is changed
def formationCallback(selection):
    formMod = formations[selection]
    print(formMod)
    return

# Destroys the row if ship inputs the button is on
def destroyRow(currentRow):
    for i in currentRow:
        i.destroy()
    return

'''
Ship data guide:
s# = Ship(name, reload, aaStat, slotEff, aaSkill, relSkil)
s# = Ship(string, int,   int,    float,   float,   float)
'''    
def createShipList(shipRowsList):

    shipList = []

    for shipRow in shipRowsList:
        s = Ship(shipRow[0], int(shipRow[1]), int(shipRow[2]), float(shipRow[3]), float(shipRow[4]), float(shipRow[5]))
        shipList.append(s)

    return shipList

# The function that formats and adds new inputs (when the button is pressed)
def addShipCallback(shipCounter, yPadding, xPadding, frm_shipInputBlockInputs, shipRowsList):

    shipCounter[0] += 1
    currentRow = []
    currentRowValues = []
    shipName = tk.StringVar()
    shipReload = tk.StringVar()
    shipAA = tk.StringVar()
    shipSlotEff = tk.StringVar()
    shipAAMod = tk.StringVar()
    shipRelMod = tk.StringVar()

    # Ship Name block
    lbl_shipInput = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Ship" ,shipCounter[0],":")
    )
    lbl_shipInput.grid(row=shipCounter[0], column=1, padx=xPadding, pady=yPadding)
    currentRow.append(lbl_shipInput)

    ent_shipNameInput = tk.Entry(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        textvariable=shipName
    )
    ent_shipNameInput.grid(row=shipCounter[0], column=2, padx=xPadding, pady=yPadding)
    currentRow.append(ent_shipNameInput)

    # Ship reload stat block
    ent_shipReload = tk.Entry(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        textvariable=shipReload
    )
    ent_shipReload.grid(row=shipCounter[0], column=3, padx=xPadding, pady=yPadding)
    currentRow.append(ent_shipReload)

    # Ship AA stat block
    ent_shipAA = tk.Entry(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        textvariable=shipAA
    )
    ent_shipAA.grid(row=shipCounter[0], column=4, padx=xPadding, pady=yPadding)
    currentRow.append(ent_shipAA)

    ## AA Gun Efficiency Block
    ent_shipSlotEf = tk.Entry(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        textvariable=shipSlotEff
    )
    ent_shipSlotEf.grid(row=shipCounter[0], column=5, padx=xPadding, pady=yPadding)
    currentRow.append(ent_shipSlotEf)

    # AA Skill Modifier Block
    ent_aaMod = tk.Entry(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        textvariable=shipAAMod
    )
    ent_aaMod.grid(row=shipCounter[0], column=6, padx=xPadding, pady=yPadding)   
    currentRow.append(ent_aaMod)

    # Reload Skill Modifier Block
    ent_relMod = tk.Entry(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        textvariable=shipRelMod
    )
    ent_relMod.grid(row=shipCounter[0], column=7, padx=xPadding, pady=yPadding)
    currentRow.append(ent_relMod)

    # Button to remove the entry
    btn_removeShipButton = tk.Button(
        master=frm_shipInputBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=10,
        text="Remove Ship",
        command=lambda: destroyRow(currentRow)
    )
    btn_removeShipButton.grid(row=shipCounter[0], column=8, padx=xPadding, pady=yPadding)
    currentRow.append(btn_removeShipButton)

    # Fills out "return" value
    currentRowValues = [
        shipName.get(),
        shipReload.get(),
        shipAA.get(),
        shipSlotEff.get(),
        shipAAMod.get(),
        shipRelMod.get()
    ]
    shipRowsList.append(currentRowValues)

    # End Callback function
    return



def calculateResultsCallback(formMod, shipRowsList, frm_resultBlockResults):

    # Creates ship list from inputs
    shipList = createShipList(shipRowsList)

    # Unimplemented
    minimumRange = None 

    # Other setup
    formationBonus = formMod

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


    # Filling in results
    currentRow = 1
    currentCol = 1

    for ship in shipList:
        # Crates ship Label
        lbl_shipName = tk.Label(
            master=frm_resultBlockResults,
            text="{}:".format(ship.getName())
        )
        lbl_shipName.grid(row=currentRow, column=currentCol, sticky=tk.W)

        # Displays result
        lbl_bestGun = tk.Label(
            master=frm_resultBlockResults,
            bg="#cdcbcb",
            fg="#3f8712",
            width=5,
            text="TEMP"
        )
        lbl_bestGun.grid(row=currentRow, column=currentCol+1, pady=2, padx=5, sticky=tk.W)
        
        currentRow += 1
        if(currentRow > 4):
            currentCol += 2
            currentRow = 1

    return