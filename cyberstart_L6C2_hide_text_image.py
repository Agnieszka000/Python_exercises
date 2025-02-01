# Cyberstart, Level 6 Challenge 2

# Hide text in the image /tmp/image.gif
# Append the word alieneye to end of the file.

with open("/tmp/image.gif", "a") as file: # "a" for append.
    add_text = file.write("alieneye") # "write" plus the word we want to add to the file.