# Sense Hat Toodler Alarm
# Version 0.01

# Import libraries for Sense Hat and other components
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
g = (0,128,0)       # Green
l = (0,225,0)       # Lime
n = (0,0,128)       # Navy
B = (0,0,255)       # Blue
m = (128,0,0)       # Maroon
r = (225,0,0)       # Red
p = (128,0,128)     # Purple
f = (225,0,225)     # Fuchsia
o = (128,0,128)     # Olive
y = (225,225,0)     # Yellow


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
#hat.clear()

# Set entire display to a single colour
#hat.clear(w)

# Set entire display to a low light mode
#hat.clear(w)
#hat.low_light = True

# Turn Off Low Light Mode
#hat.low_light = False

class Alarm():
    """ A object which represents an Alarm"""

    def __init__(self, hour, minute, interval, startcolour, countcolour, endcolour):
        self.hour = hour
        self.minute = minute
        self.interval = interval
        self.startcolour = startcolour
        self.countcolour = countcolour
        self.endcolour = endcolour


    def check_time(self):
        """This method checks if a specific hour and minute has passed
        and returns a true or false statement."""
        lh = localtime().tm_hour
        lm = localtime().tm_min
        ls = localtime().tm_sec
    
        if lh >= self.hour and lm >= self.minute and self.hour - lh >= 0 and 2 > lm - self.minute < 1:
            print(lh,lm,ls, self.hour, self.minute)
            print("True")
            return True
        else:
            print(lh,lm,ls, self.hour, self.minute)
            print("False")
            return False

    def alarm_event(self):
        """This method triggers a specific event for the alarm"""
        print("Alarm Event Triggered")

    def count_down(self):
        """This method triggers the countdown display"""

        # Setup Count Down steps. Duration of Interval to be set below.
        # Currently set to 60 steps (which will be multiplied by
        # The duration of the sleep interval)
        count = 60

        # Setup Initial Colour for Count Down
        s = 64                  # Use all 64 Pixels
        timer = []              # Create a pixel matrix

        # Fill the screen with a single colour
        for i in range(64):
            if i < s:
                timer.append(self.startcolour) # Set to White (w)
            else:
                timer.append(b)
        hat.set_pixels(timer)   # Display Pixels

        # Start Timer for number of minutes
        while localtime().tm_min >= self.minute and count > 0:

            # Update the screen based on a defined interval
            for i in range(0,60):
                timer[i] = self.countcolour
                hat.set_pixels(timer)        
                
                count = count - 1
                print(count)

                sleep(self.interval)        # Set Sleep Interval to 60 seconds
                
        else:
            print(count)
            hat.clear(self.endcolour)        # Once count down completes set screen
            
            sleep(3600)          # Keep screen colour for 3600 seconds (1 Hour) 
            
        

while True:
    # Setup wake up alarm at 6am
    # Count down timer duration is 1 hour (60 counts of 60 seconds)
    # Initial colour is White Pixels
    # Count Down and Final Pixel Colour will be in Green
    
    wakeup = Alarm(6,0,60,w,g,g)
    if wakeup.check_time() is True:
        wakeup.alarm_event()
        wakeup.count_down()
    else:
        hat.clear()

    sleep(30)                   # Check Alarm every 30 seconds.


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
