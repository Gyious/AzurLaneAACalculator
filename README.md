# AzurLaneAACalculator
Some code that calculates what AA guns go on what ships to optimize AA DPS.  Requires [Python 3.8](https://www.python.org/downloads/)

## Usage
Note: As of now, the GUI is non-functional, I am (slowly) working on making a google sheets for it instead (but that involves adapting python -> javascript)

1. Open [AACalcGuns](https://github.com/Gyious/AzurLaneAACalculator/blob/master/AACalcGuns.py) and adjust the quantities of how many of each gun you own (or want to calculate with)
  - If you are getting results with un-suitable range, I reccomend setting low range guns to 0 so it will not try to use them (such as pom pom or 12.7)
  
2. Open [AACalc](https://github.com/Gyious/AzurLaneAACalculator/blob/master/AACalc.py) and add the comp you want to optimize in the inputs section
    - Be sure to follow the ship data guide and the example inputs for formatting
    - Also change the formationBonus value towards the top
    - Always leave minimumRange as "None" - this feature is unimplemented
    - If a ship has multiple AA guns (akashi, cheshire, seattle, etc) then include them as seperate ships, but make sure their stats are identical
      - copypasting makes this easy
    
3. Run the code!
