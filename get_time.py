from time import sleep
from time import localtime
from time import gmtime

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
        while localtime().tm_min >= self.minute and count != 0:
            count = count - 1
            print(count)
            sleep(1)
        else:
            print(count)
            sleep(1)

while True:
    wakeup = Alarm(20,44)
#    if wakeup.check_time() is True:
#        wakeup.alarm_event()
    print(wakeup.count_down())
    sleep(30)
