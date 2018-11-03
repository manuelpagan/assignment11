# Manny Pagan
# Sept 24th Python Course
# Assignment 11
# Due Nov 5th



tv_characters = ["Will Byers",
                 "Tyrion Lannister",
                 "Oliver Queen",
                 "Jean Luc Picard",
                 "Malcom Reynolds",
                 "The Doctor",
                 "Sam Winchester",
                 "Sherlock Holmes"]

f = open("my_characters.txt", "w")

for index, character in enumerate(tv_characters):
    f.write("{}: {}\n".format(index+1, character))

f.close()
