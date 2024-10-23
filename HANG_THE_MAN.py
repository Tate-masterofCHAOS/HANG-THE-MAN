#HANG MAN  by Aaron, and Tate, and Martin, and Amon
import random
#List of the words
words = ["snow", "wolf", "moon", "star", "lamp", "volk", "bark", "amen","bruh", "bomb", "nuke", "noob", "beta", "paps", "sans", "wine", "dude","inky", "rose", "four", "goku","toby", "cool"]
#Variables: EVERYONE!!!!!!!!!!!!!!!!!!!!!
spa_1 = ""
spa_2 = ""
spa_3 = ""
spa_4 = ""
head = "0"
body = "|"
Larm = "/"
Rarm = "\\"
Lleg = "/"
Rleg = "\\"
Next_body_part = "Head"
Layer_7 = "  ___"
Layer_6 = " /  |"
Layer_5 = "    |"
Layer_4 = "    |"
Layer_3 = "    |"
Layer_2 = "    |"
Layer_1 = "---------"
word = random(words)
#Remember to write the input for making a guess

#Function of random 4 letter word, and add or not add a body part depending on the letter chosen:(done) Aaron Shelby
def win():
    print("Congrats ඞ you get an among us!")

def wrong():
    if Next_body_part = "head":
        Layer_5 = head + Layer_5
        print(Layer_7)
        print(Layer_6)
        print(Layer_5)
        print(Layer_4)
        print(Layer_3)
        print(Layer_2)
        print(Layer_1)
        Next_body_part = "body"
    elif Next_body_part = "body":
        Layer_4 = body + Layer_4
        print(Layer_7)
        print(Layer_6)
        print(Layer_5)
        print(Layer_4)
        print(Layer_3)
        print(Layer_2)
        print(Layer_1)
        Next_body_part = "Larm"
    elif Next_body_part = "Larm":
        Layer_4 = Larm + body + Layer_4
        print(Layer_7)
        print(Layer_6)
        print(Layer_5)
        print(Layer_4)
        print(Layer_3)
        print(Layer_2)
        print(Layer_1)
        Next_body_part = "Rarm"
    elif Next_body_part = "Rarm":
        Layer_4 = Larm + body + Rarm + Layer_4
        print(Layer_7)
        print(Layer_6)
        print(Layer_5)
        print(Layer_4)
        print(Layer_3)
        print(Layer_2)
        print(Layer_1)
        Next_body_part = "Lleg"
    elif Next_body_part = "Lleg":
        Layer_3 = Lleg + Layer_3
        print(Layer_7)
        print(Layer_6)
        print(Layer_5)
        print(Layer_4)
        print(Layer_3)
        print(Layer_2)
        print(Layer_1)
        Next_body_part = "Rleg"
    elif Next_body_part = "Rleg":
        Layer_3 = Lleg + Rleg + Layer_3
        print(Layer_7)
        print(Layer_6)
        print(Layer_5)
        print(Layer_4)
        print(Layer_3)
        print(Layer_2)
        print(Layer_1)
        Next_body_part = "ඞ"
    else: 
        print("Congratulations, your a failure ඞ")
#Print he gallows to hang the man: Tate Morgan 
print(Layer_7)
print(Layer_6)
print(Layer_5)
print(Layer_4)
print(Layer_3)
print(Layer_2)
print(Layer_1)
#Check the input: Amon Dippඞ
ans = input("Tell a letter:")
if ans == word(0):
    spa_1 = word(0)
elif ans == word(1):
    spa_2 = word(1)
elif ans == word(2):
    spa_3 = word(2)
elif ans == word(3):
    spa_4 = word(3)
else:
    wrong
print(spa_1,spa_2,spa_3,spa_4)

# Update this part when the rest are done (Variable, Function, etc.)

for i 

 # Use this one in case that doesn't works Tatedef display_gallows(incorrect_guesses):
    #layers = [
     #   "    ___",
     #   "   /   |",
     #   "       |",
     #   "       |",
     #   "       |",
     #   "       |",
    #  "   ---------"
    #]