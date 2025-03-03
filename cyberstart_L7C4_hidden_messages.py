# Cybestart Level 7 Challenge 4 - 'Hidden Messages'

# One of the agents has intercepted a file from the aliens.
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif

with open("/tmp/destroymoonbase.gif") as file:
    contents = file.read().replace("#","").replace("$","")
    print(contents)