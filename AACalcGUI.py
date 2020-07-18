import tkinter as tk
from AACalcGUIFuncs import *
from AACalcGuns import *
#from AACalc import *

# Basic setup
applicationGridRowHeights = [400, 200]
applicationGridColumnWidths = [400, 700]

window = tk.Tk()

# Creates both major frames
frm_group1 = tk.Frame(
    master=window,
    bg = "#8e7c79"
)
frm_group1.pack(fill=tk.BOTH)

frm_group2 = tk.Frame(
    master=window,
    bg="#8e7c79"
)
frm_group2.pack(fill=tk.BOTH)

# The major frame groupes i the first frame group
frm_generalInputBlock = tk.Frame(
    master=frm_group1,
    relief=tk.RAISED,
    borderwidth=1,
    #height=applicationGridRowHeights[0],
    #width=applicationGridColumnWidths[0],
    bg="yellow"
)
frm_generalInputBlock.grid(row=1, column=1, padx=10, pady=10, sticky=tk.N)

frm_shipInputBlock = tk.Frame(
    master=frm_group1,
    relief=tk.RAISED,
    borderwidth=1,
    #height=applicationGridRowHeights[0],
    #width=applicationGridColumnWidths[1],
    bg="blue"
)
frm_shipInputBlock.grid(row=1, column=2, padx=10, pady=10)

# The major frame groups in the second major frame group
frm_gunInfoBlock = tk.Frame(
    master=frm_group2,
    relief=tk.RAISED,
    borderwidth=1,
    #height=applicationGridRowHeights[1],
    #width=applicationGridColumnWidths[1],
    bg="purple"
)
frm_gunInfoBlock.pack(side=tk.LEFT, padx=10, pady=10)

frm_resultBlock = tk.Frame(
    master=frm_group2,
    relief=tk.RAISED,
    borderwidth=1,
    #height=applicationGridRowHeights[1],
    #width=applicationGridColumnWidths[0],
    bg="green"
)
frm_resultBlock.pack(side=tk.LEFT, padx=10, pady=10)

# Filling the first frame from group1
# Creating the title
frm_generalInputBlockTitle = tk.Frame(
    master=frm_generalInputBlock
)
frm_generalInputBlockTitle.pack(pady=10)

lbl_generalInputBlockTitle = tk.Label(
    master=frm_generalInputBlockTitle,
    text="General Inputs"
)
lbl_generalInputBlockTitle.pack()

# Creating the input section
# Creates the frame for the inputs
frm_generalInputBlockInputs = tk.Frame(
    master=frm_generalInputBlock,
)
frm_generalInputBlockInputs.pack(pady=10)

# Creates the first option
lbl_generalInput1 = tk.Label(
    master=frm_generalInputBlockInputs,
    text="Select formation:"
)
lbl_generalInput1.grid(row=1, column=1, padx=10, pady=5)

formationOptionVar = tk.StringVar(window)
formationOptionVar.set("Select Formation") # Default value
# Formation dictionary in AACalcGUIFuncs.py

om_generalInput1 = tk.OptionMenu(
    frm_generalInputBlockInputs,
    formationOptionVar,
    *formations,
    command=formationCallback
)
om_generalInput1.grid(row=1, column=2, padx=10, pady=5)


# Filling the 2nd frame from group1
# Creating the title frame
frm_shipInputBlockTitle = tk.Frame(
    master=frm_shipInputBlock
)
frm_shipInputBlockTitle.pack(pady=5)

# Adding the label to that frame
lbl_shipInputBlockTitle = tk.Label(
    master=frm_shipInputBlockTitle,
    text="Ship Inputs"
)
lbl_shipInputBlockTitle.pack()

# Creating the input section
# Creates the frame for the inputs
frm_shipInputBlockInputs = tk.Frame(
    master=frm_shipInputBlock,
)
frm_shipInputBlockInputs.pack(pady=5)


# Adds labels for each column for user inputs
# Ship(name, reload, aaStat, slotEff, aaSkill, relSkil)

shipCounter = [0]
shipRowsList = []
yPadding = 5
xPadding = 5

lbl_Labels = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Labels:")
    )
lbl_Labels.grid(row=0, column=1, padx=xPadding, pady=yPadding)

lbl_shipName = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Ship Name")
    )
lbl_shipName.grid(row=0, column=2, padx=xPadding, pady=yPadding)

lbl_shipReload = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Reload Stat")
    )
lbl_shipReload.grid(row=0, column=3, padx=xPadding, pady=yPadding)

lbl_aaStat = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("AA Stat")
    )
lbl_aaStat.grid(row=0, column=4, padx=xPadding, pady=yPadding)

lbl_efficiency = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Slot Efficiency")
    )
lbl_efficiency.grid(row=0, column=5, padx=xPadding, pady=yPadding)

lbl_aaMod = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("AA Skill Mod")
    )
lbl_aaMod.grid(row=0, column=6, padx=xPadding, pady=yPadding)

lbl_reloadMod = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Reload Skill Mod")
    )
lbl_reloadMod.grid(row=0, column=7, padx=xPadding, pady=yPadding)

lbl_remButton = tk.Label(
        master=frm_shipInputBlockInputs,
        text=("Removal Button")
    )
lbl_remButton.grid(row=0, column=8, padx=xPadding, pady=yPadding)

# Creates a button to add new ships to the input section
# Creates the frame for the button
frm_addShipButton = tk.Frame(
    master=frm_shipInputBlock
)
frm_addShipButton.pack(pady=10)

# Creates the button
btn_addShipButton = tk.Button(
    master=frm_addShipButton,
    text="Add Ship",
    command=lambda: addShipCallback(shipCounter, yPadding, xPadding, frm_shipInputBlockInputs, shipRowsList)
)
btn_addShipButton.pack(pady=10)


# Section for group 2 frames
# Filing first frame from group 2
# (gun selection)
 
# Creating a title
frm_gunInfoBlockTitle = tk.Frame(
    master=frm_gunInfoBlock
)
frm_gunInfoBlockTitle.pack(pady=10, padx=10)

lbl_gunInfoBlockTitle = tk.Label(
    master=frm_gunInfoBlockTitle,
    text="Gun Selection\n(quantity)"
)
lbl_gunInfoBlockTitle.pack()

# Creating a frame for the guns:
frm_gunInfoBlockInputs = tk.Frame(
    master=frm_gunInfoBlock
)
frm_gunInfoBlockInputs.pack(pady=5, padx=10)

# Filling in guns
currentRow = 1
currentCol = 1

for gun in gunList:
    # Crates Label
    lbl_gunName = tk.Label(
        master=frm_gunInfoBlockInputs,
        text="{}:".format(gun.getName())
    )
    lbl_gunName.grid(row=currentRow, column=currentCol, sticky=tk.W)

    # Creates input
    gunEntryValue = tk.StringVar(window)
    gunEntryValue.set(0)
    ent_gunAmount = tk.Entry(
        master=frm_gunInfoBlockInputs,
        bg="#cdcbcb",
        fg="#3f8712",
        width=5,
        textvariable = gunEntryValue
    )
    ent_gunAmount.grid(row=currentRow, column=currentCol+1, pady=2, padx=5, sticky=tk.W)
        
    currentRow += 1
    if(currentRow > 6):
        currentCol += 2
        currentRow = 1
    


# Filling group 2 frame 2 (results)
# Creating a title
frm_resultBlockTitle = tk.Frame(
    master=frm_resultBlock
)
frm_resultBlockTitle.pack(pady=10, padx=10)

lbl_resultBlockTitle = tk.Label(
    master=frm_resultBlockTitle,
    text="Results"
)
lbl_resultBlockTitle.pack()

# Creating a frame for the results
frm_resultBlockResults = tk.Frame(
    master=frm_resultBlock
)
frm_resultBlockResults.pack(pady=5, padx=10)


# Creating a frame for other results
frm_otherResults = tk.Frame(
    master=frm_resultBlock
)
frm_otherResults.pack(pady=10, padx=10)

# Filling in other results
lbl_displayRangeLabel = tk.Label(
    master=frm_otherResults,
    text="Range:"
)
lbl_displayRangeLabel.grid(row=1, column=1)

lbl_displayRange = tk.Label(
    master=frm_otherResults,
    text="TEMP"
)
lbl_displayRange.grid(row=1, column=2)

lbl_displayDPSLabel = tk.Label(
    master=frm_otherResults,
    text="DPS:"
)
lbl_displayDPSLabel.grid(row=2, column=1)

lbl_displayDPS = tk.Label(
    master=frm_otherResults,
    text="TEMP"
)
lbl_displayDPS.grid(row=2, column=2)


# Adds a calculate button
btn_calculateResults = tk.Button(
    master=frm_resultBlock,
    text="CALCULATE",
    command=lambda: calculateResultsCallback(formations[formationOptionVar.get()], shipRowsList, frm_resultBlockResults)
)
btn_calculateResults.pack(pady=10, padx=10)







'''
# Color references for different types of items
label=tk.Label(
    master=frm_generalInputBlock,
    text=":ALKJF"
)
label.pack()
'''
'''
greeting = tk.Label(text="TEST",
                    bg = "#8e7c79",
                    fg = "#e5ffd5",
                    width = 25,
                    height = 15)
greeting.pack()

'''

'''

button = tk.Button(text = "Test Button",
                    bg = "#d04129",
                    fg = "#e5ffd5",
                    width = 15,
                    height = 1)

button.pack()

entry = tk.Entry(bg="#cdcbcb",
                fg="#3f8712",
                width=7)

entry.pack()
'''

window.mainloop()

