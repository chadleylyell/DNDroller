import board, terminalio, displayio, digitalio, random, supervisor
from adafruit_display_text import label
from adafruit_ssd1351 import SSD1351
from adafruit_debouncer import Debouncer
from time import sleep
from adafruit_bitmapsaver import save_pixels

# Disables auto-reload
supervisor.runtime.autoreload = False

# Release any resources currently in use for the displays
displayio.release_displays()
# Display pins
spi = board.SPI()
tft_cs = board.A0
tft_dc = board.A1
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7, baudrate=16000000)
display = SSD1351(display_bus, width=128, height=128)

# Make the display context
screen = displayio.Group()
display.show(screen)

row1_variable = 40
row2_variable = 63
row3_variable = 86
row4_variable = 109

diceScale = 2
rollScale = 2
col1_variable = 2    # x axis
col2_variable = 60   # x axis 

# Colors
white = 0xFFFFFF
purple = 0x7846AD
red = 0xff0000
blue = 0x0000ff
green = 0x00ff00
orange = 0xff7300
pink = 0xff00f5
teal = 0x008080
yellow = 0xf8ff00
grey = 0x373737

fileOpen = open("color.txt")
userPreference = fileOpen.read()

def whiteGreyDefine():
    if userPreference == "yellow":
        return grey
    else:
        return white

def colorDefine():
    if userPreference == "purple":
        return purple
    if userPreference == "red":
        return red
    if userPreference == "blue":
        return blue
    if userPreference == "green":
        return green
    if userPreference == "orange":
        return orange
    if userPreference == "pink":
        return pink
    if userPreference == "teal":
        return teal
    if userPreference == "yellow":
        return yellow
def colorUpdate(newColor, whiteBlackText):
    D4_highlight.color = whiteBlackText
    D6_highlight.color = whiteBlackText
    D8_highlight.color = whiteBlackText
    D10_highlight.color = whiteBlackText
    D12_highlight.color = whiteBlackText
    D20_highlight.color = whiteBlackText
    D100_highlight.color = whiteBlackText
    perc_highlight.color = whiteBlackText
    colorSelect_highlight.color = whiteBlackText
    #
    D4_highlight.background_color = newColor
    D6_highlight.background_color = newColor
    D8_highlight.background_color = newColor
    D10_highlight.background_color = newColor
    D12_highlight.background_color = newColor
    D20_highlight.background_color = newColor
    D100_highlight.background_color = newColor
    perc_highlight.background_color = newColor
    colorSelect_highlight.background_color = newColor
    #
    header.color = newColor
    roll_header.color = newColor



userColor = colorDefine()
print(userColor)
# Create text labels for screen 1 | Section 1
header = label.Label(terminalio.FONT, text="Please choose an\noption:", color=colorDefine(), x=2, y=4)

D4_text = label.Label(terminalio.FONT, text="D4", scale=diceScale, color=white, x=col1_variable, y=row1_variable)
D6_text = label.Label(terminalio.FONT, text="D6", scale=diceScale, color=white, x=col1_variable, y=row2_variable)
D8_text = label.Label(terminalio.FONT, text="D8", scale=diceScale, color=white, x=col1_variable, y=row3_variable)
D10_text = label.Label(terminalio.FONT, text="D10", scale=diceScale, color=white, x=col1_variable, y=row4_variable)
D12_text = label.Label(terminalio.FONT, text="D12", scale=diceScale, color=white, x=col2_variable, y=row1_variable)
D20_text = label.Label(terminalio.FONT, text="D20", scale=diceScale, color=white, x=col2_variable, y=row2_variable)
D100_text = label.Label(terminalio.FONT, text="D100", scale=diceScale, color=white, x=col2_variable, y=row3_variable)
perc_text = label.Label(terminalio.FONT, text="%", scale=diceScale, color=white, x=col2_variable, y=row4_variable)
colorSelect_text = label.Label(terminalio.FONT, text="C", color=white, x=120, y=120)

# Create highlight labels for screen 1 | Section 2
D4_highlight = label.Label(terminalio.FONT, text="D4", background_color=colorDefine(), scale=diceScale, color=whiteGreyDefine(), x=col1_variable, y=row1_variable)
D6_highlight = label.Label(terminalio.FONT, text="D6", background_color=colorDefine(), scale=diceScale, color=whiteGreyDefine(), x=col1_variable, y=row2_variable)
D8_highlight = label.Label(terminalio.FONT, text="D8", background_color=colorDefine(), scale=diceScale, color=whiteGreyDefine(), x=col1_variable, y=row3_variable)
D10_highlight = label.Label(terminalio.FONT, text="D10", background_color=colorDefine(), scale=diceScale, color=whiteGreyDefine(), x=col1_variable, y=row4_variable)
D12_highlight = label.Label(terminalio.FONT, text="D12", background_color=colorDefine(), scale=diceScale, color=whiteGreyDefine(), x=col2_variable, y=row1_variable)
D20_highlight = label.Label(terminalio.FONT, text="D20", background_color=colorDefine(), scale=diceScale, color=whiteGreyDefine(), x=col2_variable, y=row2_variable)
D100_highlight = label.Label(terminalio.FONT, text="D100", scale=diceScale, background_color=colorDefine(), color=whiteGreyDefine(), x=col2_variable, y=row3_variable)
perc_highlight = label.Label(terminalio.FONT, text="%", scale=diceScale, background_color=colorDefine(), color=whiteGreyDefine(), x=col2_variable, y=row4_variable)
colorSelect_highlight = label.Label(terminalio.FONT, text="C", background_color=colorDefine(), color=whiteGreyDefine(), x=120, y=122)

section1 = displayio.Group()
section2 = displayio.Group()
for t in (header, D4_text, D6_text, D8_text, D10_text, D12_text, D20_text, D100_text, perc_text, colorSelect_text):
    section1.append(t)
screen.append(section1)

for l in (D4_highlight, D6_highlight, D8_highlight, D10_highlight, D12_highlight, D20_highlight, D100_highlight, perc_highlight, colorSelect_highlight):
    section2.append(l)
    D4_highlight.hidden = True
    D6_highlight.hidden = True
    D8_highlight.hidden = True
    D10_highlight.hidden = True
    D12_highlight.hidden = True
    D20_highlight.hidden = True
    colorSelect_highlight.hidden = True
    D100_highlight.hidden = True
    perc_highlight.hidden = True
screen.append(section2)
D4_highlight.hidden = False

# section1.hidden = True
# section2.hidden = True



# Create text labels for roll selection

roll_header = label.Label(terminalio.FONT, text="Number of rolls:", color=colorDefine(), x=2, y=4)
brackets = label.Label(terminalio.FONT, text="<    >", scale=rollScale, color=white, x=25, y=40)
instruction = label.Label(terminalio.FONT, text="Press enter to roll.", color=white, x=5, y=80)
cancel = label.Label(terminalio.FONT, text="Up to cancel", color=white, x=58, y=122)

rollX = 56
rollY = 40
# Create text labels for numbers
rollLabel = label.Label(terminalio.FONT, text="1", scale=rollScale, color=white, x=rollX, y=rollY)

rollSelectScreen = displayio.Group()

for s in (roll_header, brackets, instruction, cancel, rollLabel):
    rollSelectScreen.append(s)
    rollSelectScreen.hidden = True
screen.append(rollSelectScreen)

# Create text labels for the final roll display.

row1_var = 25
row2_var = 50
row3_var = 75

col1_var = 2    # x axis
col2_var = 45   # x axis 
col3_var = 88

rolledScreen = displayio.Group()
firstLast = displayio.Group()

rolledHeader = label.Label(terminalio.FONT, text="", color=colorDefine(), x=2, y=4)
continueSentence = label.Label(terminalio.FONT, text="Enter to continue", color=white, x=2, y=122)
firstLabel = label.Label(terminalio.FONT, text="First", color=red, x=2, y=100)
lastLabel = label.Label(terminalio.FONT, text="Last", color=blue, x=45, y=100)

rolled1 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col1_var, y=row1_var)
rolled2 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col2_var, y=row1_var)
rolled3 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col3_var, y=row1_var)
rolled4 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col1_var, y=row2_var)
rolled5 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col2_var, y=row2_var)
rolled6 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col3_var, y=row2_var)
rolled7 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col1_var, y=row3_var)
rolled8 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col2_var, y=row3_var)
rolled9 = label.Label(terminalio.FONT, text="", scale=2, color=white, x=col3_var, y=row3_var)

for g in (rolledHeader, continueSentence, rolled1, rolled2, rolled3, rolled4, rolled5, rolled6, rolled7, rolled8, rolled9):
    rolledScreen.append(g)
    rolledScreen.hidden = True
screen.append(rolledScreen)

for k in (firstLabel, lastLabel):
    firstLast.append(k)
rolledScreen.append(firstLast)

def setup_button(pin, pull=digitalio.Pull.UP):
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = pull
    return button

button_a = setup_button(board.D25)    # Up button        <Orange Wire>   (D25)
button_b = setup_button(board.D24)    # Right button     <Green Wire>    (D24)
button_c = setup_button(board.A3)     # Down button      <Yellow Wire>   (A3)
button_d = setup_button(board.D9)     # Left button      <Black Wire>    (D5)
button_e = setup_button(board.A2)     # Center button    <Blue Wire>     (A2)

Up = Debouncer(button_a)
Right = Debouncer(button_b)
Down = Debouncer(button_c)
Left = Debouncer(button_d)
Enter = Debouncer(button_e)

def hideRollLabels():
    rollLabel.hidden = True

def firstLastHighlight(choice):
    if choice == 1:
        rolled1.color = white
    if choice == 2:
        rolled1.color = red
        rolled2.color = blue
    if choice == 3:
        rolled1.color = red
        rolled3.color = blue
    if choice == 4:
        rolled1.color = red
        rolled4.color = blue
    if choice == 5:
        rolled1.color = red
        rolled5.color = blue
    if choice == 6:
        rolled1.color = red
        rolled6.color = blue
    if choice == 7:
        rolled1.color = red
        rolled7.color = blue
    if choice == 8:
        rolled1.color = red
        rolled8.color = blue
    if choice == 9:
        rolled1.color = red
        rolled9.color = blue

def clearDice():
    rolledHeader.text = ""
    rolled1.text = ""
    rolled2.text = ""
    rolled3.text = ""
    rolled4.text = ""
    rolled5.text = ""
    rolled6.text = ""
    rolled7.text = ""
    rolled8.text = ""
    rolled9.text = ""

    rolled1.color = white
    rolled2.color = white
    rolled3.color = white
    rolled4.color = white
    rolled5.color = white
    rolled6.color = white
    rolled7.color = white
    rolled8.color = white
    rolled9.color = white

def displayDice(choice, dice, one, two, three, four, five, six, seven, eight, nine):
    clearDice()
    firstLastHighlight(choice)
    if choice == 1:
        rolledHeader.text = f"Rolled {dice} {choice} time:"
        rolled1.text = f"{one}"
        firstLast.hidden = True
        rolledScreen.hidden = False
    else:
        rolledHeader.text = f"Rolled {dice} {choice} times:"
        rolled1.text = f"{one}"
        rolled2.text = f"{two}"
        rolled3.text = f"{three}"
        rolled4.text = f"{four}"
        rolled5.text = f"{five}"
        rolled6.text = f"{six}"
        rolled7.text = f"{seven}"
        rolled8.text = f"{eight}"
        rolled9.text = f"{nine}"
        firstLast.hidden = False
        rolledScreen.hidden = False
    while True:
        Up.update()
        Right.update()
        Down.update()
        Left.update()
        Enter.update()

        if Enter.fell:
            rolledScreen.hidden = True
            break

def rollDice(rollChoice, dice): # one = rollChoice (user selected 1-9) from rollSelect() | two = dice from rollSelect() and what's highlighted upon user select in main loop. 
    rollingCount = 0
    roll = ["", "", "", "", "", "", "", "", ""]
    while True:
        if rollingCount == rollChoice:
            D1 = roll[0]
            D2 = roll[1]
            D3 = roll[2]
            D4 = roll[3]
            D5 = roll[4]
            D6 = roll[5]
            D7 = roll[6]
            D8 = roll[7]
            D9 = roll[8]
            rollSelectScreen.hidden = True
            displayDice(rollChoice, dice, roll[0], roll[1], roll[2], roll[3], roll[4], roll[5], roll[6], roll[7], roll[8])
            break

        if dice == "D4":
            RD = random.randint(1,4)
            if RD == 1:
                roll[rollingCount] = "1"
                rollingCount += 1
            if RD == 2:
                roll[rollingCount] = "2"
                rollingCount += 1
            if RD == 3:
                roll[rollingCount] = "3"
                rollingCount += 1
            if RD == 4:
                roll[rollingCount] = "4"
                rollingCount += 1
        if dice == "D6":
            RD = random.randint(1,6)
            roll[rollingCount] = f"{RD}"
            rollingCount += 1

        if dice == "D8":
            RD = random.randint(1,8)
            roll[rollingCount] = f"{RD}"
            rollingCount += 1

        if dice == "D10":
            RD = random.randint(1,10)
            roll[rollingCount] = f"{RD}"
            rollingCount += 1

        if dice == "D12":
            RD = random.randint(1,12)
            roll[rollingCount] = f"{RD}"
            rollingCount += 1

        if dice == "D20":
            RD = random.randint(1,20)
            roll[rollingCount] = f"{RD}"
            rollingCount += 1

        if dice == "D100":
            RD = random.randint(1,100)
            roll[rollingCount] = f"{RD}"
            rollingCount += 1


def rollSelect(var):
    dice = var
    roll_highlight = "one"
    rollSelectScreen.hidden = False
    hideRollLabels()
    rollLabel.text = "1"
    rollLabel.hidden = False
    while True:
        Up.update()
        Right.update()
        Down.update()
        Left.update()
        Enter.update()

        #
        # Exit
        #
        if Up.fell:
            rollSelectScreen.hidden = True
            break
        #
        # One
        #
        if Right.fell and roll_highlight == "one":
            roll_highlight = "two"
            rollLabel.text = "2"
            continue
        if Left.fell and roll_highlight == "one":
            roll_highlight = "nine"
            rollLabel.text = "9"
            continue
        if Enter.fell and roll_highlight == "one":
            rollChoice = 1
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Two
        #
        if Right.fell and roll_highlight == "two":
            roll_highlight = "three"
            rollLabel.text = "3"
            continue
        if Left.fell and roll_highlight == "two":
            roll_highlight = "one"
            rollLabel.text = "1"
            continue
        if Enter.fell and roll_highlight == "two":
            rollChoice = 2
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Three
        #
        if Right.fell and roll_highlight == "three":
            roll_highlight = "four"
            rollLabel.text = "4"
            continue
        if Left.fell and roll_highlight == "three":
            roll_highlight = "two"
            rollLabel.text = "2"
            continue
        if Enter.fell and roll_highlight == "three":
            rollChoice = 3
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Four
        #
        if Right.fell and roll_highlight == "four":
            roll_highlight = "five"
            rollLabel.text = "5"
            continue
        if Left.fell and roll_highlight == "four":
            roll_highlight = "three"
            rollLabel.text = "3"
            continue
        if Enter.fell and roll_highlight == "four":
            rollChoice = 4
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Five
        #
        if Right.fell and roll_highlight == "five":
            roll_highlight = "six"
            rollLabel.text = "6"
            continue
        if Left.fell and roll_highlight == "five":
            roll_highlight = "four"
            rollLabel.text = "4"
            continue
        if Enter.fell and roll_highlight == "five":
            rollChoice = 5
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Six
        #
        if Right.fell and roll_highlight == "six":
            roll_highlight = "seven"
            rollLabel.text = "7"
            continue
        if Left.fell and roll_highlight == "six":
            roll_highlight = "five"
            rollLabel.text = "5"
            continue
        if Enter.fell and roll_highlight == "six":
            rollChoice = 6
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Seven
        #
        if Right.fell and roll_highlight == "seven":
            roll_highlight = "eight"
            rollLabel.text = "8"
            continue
        if Left.fell and roll_highlight == "seven":
            roll_highlight = "six"
            rollLabel.text = "6"
            continue
        if Enter.fell and roll_highlight == "seven":
            rollChoice = 7
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Eight
        #
        if Right.fell and roll_highlight == "eight":
            roll_highlight = "nine"
            rollLabel.text = "9"
            continue
        if Left.fell and roll_highlight == "eight":
            roll_highlight = "seven"
            rollLabel.text = "7"
            continue
        if Enter.fell and roll_highlight == "eight":
            rollChoice = 8
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break
        #
        # Nine
        #
        if Right.fell and roll_highlight == "nine":
            roll_highlight = "one"
            rollLabel.text = "1"
            continue
        if Left.fell and roll_highlight == "nine":
            roll_highlight = "eight"
            rollLabel.text = "8"
            continue
        if Enter.fell and roll_highlight == "nine":
            rollChoice = 9
            rollSelectScreen.hidden = True
            rollDice(rollChoice, dice)
            break



def highlight_D4():
    D4_highlight.hidden = False
    D6_highlight.hidden = True
    D12_highlight.hidden = True
    D20_highlight.hidden = True
    colorSelect_highlight.hidden = True
    perc_highlight.hidden = True

def highlight_D6():
    D6_highlight.hidden = False
    D4_highlight.hidden = True
    D8_highlight.hidden = True
    D20_highlight.hidden = True

def highlight_D8():
    D8_highlight.hidden = False
    D6_highlight.hidden = True
    D10_highlight.hidden = True
    D100_highlight.hidden = True

def highlight_D10():
    D10_highlight.hidden = False
    D8_highlight.hidden = True
    D12_highlight.hidden = True
    perc_highlight.hidden = True

def highlight_D12():
    D12_highlight.hidden = False
    D4_highlight.hidden = True
    D10_highlight.hidden = True
    D20_highlight.hidden = True

def highlight_D20():
    D20_highlight.hidden = False
    D6_highlight.hidden = True
    D12_highlight.hidden = True
    D100_highlight.hidden = True

def highlight_D100():
    D100_highlight.hidden = False
    D8_highlight.hidden = True
    D20_highlight.hidden = True
    perc_highlight.hidden = True

def highlight_perc():
    perc_highlight.hidden = False
    D4_highlight.hidden = True
    D10_highlight.hidden = True
    D100_highlight.hidden = True
    colorSelect_highlight.hidden = True

def highlight_C():
    colorSelect_highlight.hidden = False
    perc_highlight.hidden = True

highlight = "D4"
while True:
    Up.update()
    Right.update()
    Down.update()
    Left.update()
    Enter.update()

    #
    # D4 Highlighted
    #
    if Up.fell and highlight == "D4":
        highlight = "perc"
        highlight_perc()
        continue
    if Right.fell and highlight == "D4":
        highlight = "D12"
        highlight_D12()
        continue
    if Down.fell and highlight == "D4":
        highlight = "D6"
        save_pixels("/screenshot.bmp", display)
        # D20_text.background_color = red
        # D20_highlight.background_color = None # THIS WORKS
        highlight_D6()
        continue
    if Left.fell and highlight == "D4":
        highlight = "D12"
        highlight_D12()
        continue
    if Enter.fell and highlight == "D4":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue


    #
    # D6 Highlighted
    #
    if Up.fell and highlight == "D6":
        highlight = "D4"
        highlight_D4()
        continue
    if Right.fell and highlight == "D6":
        highlight = "D20"
        highlight_D20()
        continue
    if Down.fell and highlight == "D6":
        highlight = "D8"
        highlight_D8()
        continue
    if Left.fell and highlight == "D6":
        highlight = "D20"
        highlight_D20()
        continue
    if Enter.fell and highlight == "D6":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue


    #
    # D8 Highlighted
    #
    if Up.fell and highlight == "D8":
        highlight = "D6"
        highlight_D6()
        continue
    if Right.fell and highlight == "D8":
        highlight = "D100"
        highlight_D100()
        continue
    if Down.fell and highlight == "D8":
        highlight = "D10"
        highlight_D10()
        continue
    if Left.fell and highlight == "D8":
        highlight = "D100"
        highlight_D100()
        continue
    if Enter.fell and highlight == "D8":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue



    #
    # D10 Highlighted
    #
    if Up.fell and highlight == "D10":
        highlight = "D8"
        highlight_D8()
        continue
    if Right.fell and highlight == "D10":
        highlight = "perc"
        highlight_perc()
        continue
    if Down.fell and highlight == "D10":
        highlight = "D12"
        highlight_D12()
        continue
    if Left.fell and highlight == "D10":
        highlight = "perc"
        highlight_perc()
        continue
    if Enter.fell and highlight == "D10":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue


    #
    # D12 Highlighted
    #
    if Up.fell and highlight == "D12":
        highlight = "D10"
        highlight_D10()
        continue
    if Right.fell and highlight == "D12":
        highlight = "D4"
        highlight_D4()
        continue
    if Down.fell and highlight == "D12":
        highlight = "D20"
        highlight_D20()
        continue
    if Left.fell and highlight == "D12":
        highlight = "D4"
        highlight_D4()
        continue
    if Enter.fell and highlight == "D12":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue


    #
    # D20 Highlighted
    #
    if Up.fell and highlight == "D20":
        highlight = "D12"
        highlight_D12()
        continue
    if Right.fell and highlight == "D20":
        highlight = "D6"
        highlight_D6()
        continue
    if Down.fell and highlight == "D20":
        highlight = "D100"
        highlight_D100()
        continue
    if Left.fell and highlight == "D20":
        highlight = "D6"
        highlight_D6()
        continue
    if Enter.fell and highlight == "D20":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue


    #
    # D100 Highlighted
    #
    if Up.fell and highlight == "D100":
        highlight = "D20"
        highlight_D20()
        continue
    if Right.fell and highlight == "D100":
        highlight = "D8"
        highlight_D8()
        continue
    if Down.fell and highlight == "D100":
        highlight = "perc"
        highlight_perc()
        continue
    if Left.fell and highlight == "D100":
        highlight = "D8"
        highlight_D8()
        continue
    if Enter.fell and highlight == "D100":
        section1.hidden = True
        section2.hidden = True
        sleep(.1)
        rollSelect(highlight)
        sleep(.1)
        section1.hidden = False
        section2.hidden = False
        continue


    #
    # perc Highlighted
    #
    if Up.fell and highlight == "perc":
        highlight = "D100"
        highlight_D100()
        continue
    if Right.fell and highlight == "perc":
        highlight = "C"
        highlight_C()
        continue
    if Down.fell and highlight == "perc":
        highlight = "D4"
        highlight_D4()
        continue
    if Left.fell and highlight == "perc":
        highlight = "D10"
        highlight_D10()
        continue
    if Enter.fell and highlight == "perc":
        perc_roll()
        continue


    #
    # C Highlighted
    #
    if Up.fell and highlight == "C":
        continue
    if Right.fell and highlight == "C":
        continue
    if Down.fell and highlight == "C":
        highlight = "D4"
        highlight_D4()
        continue
    if Left.fell and highlight == "C":
        highlight = "perc"
        highlight_perc()
        continue
    if Enter.fell and highlight == "C":
        colorSelect()
        continue