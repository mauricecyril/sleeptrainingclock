# Sense Hat Countdown Test
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

class Alarm():
    """ A object which represents an Alarm"""

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


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
        count = 60
        s = 64
        timer = []
        for i in range(64):
            if i < s:
                timer.append(w)
            else:
                timer.append(b)
        hat.set_pixels(timer)
        
        while localtime().tm_min >= self.minute and count > 0:
            for i in range(0,60):
                timer[i] = g
                hat.set_pixels(timer)        
                
                count = count - 1
                print(count)

                sleep(1)
                
        else:
            print(count)
            hat.clear(g)
            
            sleep(30)

while True:
    wakeup = Alarm(20,5)
#    if wakeup.check_time() is True:
#        wakeup.alarm_event()
    wakeup.count_down()
    sleep(30)
