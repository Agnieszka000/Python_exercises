import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    daytime = s[-2:]
    hour = s[0:2]
    mins_secs = s[3:8]

    if daytime == "AM" and hour == "12":
        return (f"00"+":"+mins_secs)
    elif daytime == "AM":
        return (s[0:8])
    elif daytime == "PM":
        match hour:
            case "01":
                return (f"13"+":"+mins_secs)
            case "02":
                return (f"14"+":"+mins_secs)
            case "03":
                return (f"15"+":"+mins_secs)
            case "04":
                return (f"16"+":"+mins_secs)
            case "05":
                return (f"17"+":"+mins_secs)
            case "06":
                return (f"18"+":"+mins_secs)
            case "07":
                return (f"19"+":"+mins_secs)
            case "08":
                return (f"20"+":"+mins_secs)
            case "09":
                return (f"21"+":"+mins_secs)
            case "10":
                return (f"22"+":"+mins_secs)
            case "11":
                return (f"23"+":"+mins_secs)
            case "12":
                return (s[0:8])            
            
s = "12:45:54PM"
result = timeConversion(s)
print(result)