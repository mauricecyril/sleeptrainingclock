from time import sleep
from time import localtime
from time import gmtime


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
    checktime(*gettime(), checkhour=00, checkminute=35)
    print("Initial Check")
    print(checktime)

    print("Checking again")
    if checktime(*gettime(), checkhour=00, checkminute=35) is True:
        print("Pass in While Statement - Getting Late")
    else:
        print("Fail in While Statement - Still Time")


    sleep(5)
