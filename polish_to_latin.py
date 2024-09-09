# This is a script to convert words into lowercase words, and turn Polish characters (e.g., ą, ć) into their Latin equivalents (e.g., a, c).

pl_file = "my_ditionary.txt"                # source file containing words with Polish characters
latin_file = "my_dictionary_clean.txt"       # output file for words without Polish characters

with open(pl_file, "r", encoding="UTF-8") as file, open (latin_file, "w") as new_file:
    file_content = file.read()
    pl_words = file_content.lower().split()     # all letters are swapped by their lowercase equivalents, and the file is split into words
    latin_words = []                            # here I create a list to add the words with only Latin characters using the "append()" method
    
    for pl_word in pl_words:
        # here goes the Polish characters replacement
        latin_word = pl_word.replace("ą","a").replace("ć","c").replace("ę","e").replace("ł","l").replace("ń","n").replace("ó","o").replace("ś","s").replace("ź","z").replace("ż","z")
        #print(latin_word)
        # here I append each word to the "latin_words" list
        latin_words.append(latin_word)
    print(latin_words)

    # I write the words from the list to the output file separating them with a new line
    new_file.write("\n".join(latin_words))