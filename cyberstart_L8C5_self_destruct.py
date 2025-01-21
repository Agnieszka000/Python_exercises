# Cyberstart Platform - Level 8, Challenge 5 - "Self Destruct"

# Write a script thaht makes HTTP requests to the server http://127.0.0.1/selfdestruct
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the responsse and stop your attack once you see the flag.

import urllib.request, urllib.error, urllib.parse
import re

while True:
    response = urllib.request.urlopen("http://127.0.0.1:8082/selfdestuct")
    html = response.read().decode()
    numberA = re.search('<div class="numberA>\s*(\d+)\s*</div>', html)
    numberB = re.search('<div class="numberB>\s*(\d+)\s*</div>', html)
    if numberA.group(1) != numberB.group(1):
        continue
    else:
        print("There's a match!")
        print(f"NumberA: {numberA.group(1)}, NumberB: {numberB.group(1)}")
        print(html)
        break