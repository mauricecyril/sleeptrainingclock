# Sense Hat Toodler Alarm
# Version 0.01

# Import libraries for Sense Hat and other components
from colorsys import hsv_to_rgb
from time import sleep
from time import localtime
from time import gmtime


# Change sense_emu to sense_hat if using this code on a physical Sense HAT
from sense_emu import SenseHat

# Create a variable for calling the Sense HAT and initiate Sense HAT
hat = SenseHat()

# Define Colours
w = (255, 255, 255) # White
b = (0,0,0)         # Black

# Set Pixel Matrix
#piximage = [
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,
#    b, b, b, b, b, b, b, b,


# Clear the entire display
hat.clear()

# Set entire display to a single colour
hat.clear(w)

# Set entire display to a low light mode
hat.clear(w)
hat.low_light = True

# Turn Off Low Light Mode
hat.low_light = False


def gettime():
    """This function pulls the current time and returns a tuple (h, m, s)"""
    local_hour = localtime().tm_hour
    local_minute = localtime().tm_min
    local_second = localtime().tm_sec
    utc_hour = gmtime().tm_hour
    utc_minute = gmtime().tm_min
    utc_second = gmtime().tm_sec

    # Return a tuple [0 = hour, 1 = minute, 2 = second]
    return(local_hour, local_minute, local_second)

def checktime(lh,lm,ls,checkhour,checkminute):
    """This function checks if a specific hour or minute has passed and returns
    a true or false statement. (Ref Hour, Ref Min, Ref Sec, Check Hour, Check Min)"""
    if lh >= checkhour and lm >= checkminute:
        print(lh,lm,ls, checkhour, checkminute)
        print("Pass in Function")
        return True
    else:
        print(lh,lm,ls,checkhour, checkminute)
        print("Fail in Function")
        return False


while True:
    # Pass function gettime() as a variable argument to check time function
    # If true print getting late, if false still within time
    if checktime(*gettime(), checkhour=00, checkminute=35) is True:
        print("Pass in While Statement - Getting Late")
    else:
        print("Fail in While Statement - Still Time")

    sleep(5)


# Todo
# 1) When user presses button, the count down timer for sleep time starts
#       Parent can set sleep time count down (night light mode) or preset time
#       must transition to low light mode.
# 2) Need several check times
#       Morning Time check -> for more sophistication can add a motion sensor
#           If after 5am and motion sensor is triggered begin stay in room mode
#       Stay in room mode
#       Count down to leave room -> Colour change to blue or green once given ok
# 3) Parents should be able to overide leave room and extend or end early
# 4) Need to build method trigger via wifi too.
# 5) Optional method to allow child to interact
