# Manny Pagan
# Sept 24th Python Course
# Assignment 11
# Due Nov 5th



rainbow = {
  "name": "Roy G. Biv",
  "colors": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
  "end": "Pot Of Gold!",
  "number": "double",
  "count": 2,
  "gold": 100
}

def problem_3():
    print("The rainbow's name is", rainbow["name"])
    if rainbow["end"] == "Pot Of Gold!":
        print("I'll be taking that gold!")
    else:
        print("No money for me!")
    for color in rainbow["colors"]:
        if color is not "indigo":
            print(color)
        else:
            print("What color is indigo?")
    gold_amount = rainbow["count"] + rainbow["gold"]
    print(gold_amount)
    persons = 1
    split_gold = rainbow["gold"] / persons
    print(split_gold)

problem_3()
