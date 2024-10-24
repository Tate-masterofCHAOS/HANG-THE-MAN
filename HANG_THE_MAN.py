#HANG MAN by Aaron, and Tate, and Martin, and Amon
import random

#Variables: EVERYONE!!!!!!!!!!!!!!!!!!!!!
spa_1 = "1"
spa_2 = "2"
spa_3 = "3"
spa_4 = "4"     

#Remember to write the input for making a guess

#Function of random 4 letter word, and add or not add a body part depending on the letter chosen:(done) Aaron Shelby
def win():
    print("Congrats, you get ඞamongiඞ !")

def wrong():
    head = "0"
    body = "|"
    Larm = "/"
    Rarm = "\\"
    Lleg = "/"
    Rleg = "\\"
    Layer_7 = "  __"
    Layer_6 = " /  |"
    Layer_5 = "   |"
    Layer_4 = " |  "
    Layer_3 = "  |"
    Layer_2 = "    |"
    Layer_1 = "---------"
    Next_body_part = "head"
    for i in range(1):
        if Next_body_part == "head":
            Layer_5 = head + Layer_5
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            Next_body_part = "body"
        elif Next_body_part == "body":
            Layer_4 = body + Layer_4
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            Next_body_part = "Larm"
        elif Next_body_part == "Larm":
            Layer_4 = Larm + body + Layer_4
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            Next_body_part = "Rarm"
        elif Next_body_part == "Rarm":
            Layer_4 = Larm + body + Rarm + Layer_4
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            Next_body_part = "Lleg"
        elif Next_body_part == "Lleg":
            Layer_3 = Lleg + Layer_3
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            Next_body_part = "Rleg"
        elif Next_body_part == "Rleg":
            Layer_3 = Lleg + Rleg + Layer_3
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
        else: 
            print("Congratulations, your a failure ඞ")
#Print the gallows to hang the man: Tate Morgan 

#Check the input: Amon Dippඞ and loop the guesses: Martin
while True:
    ans = input("Tell a letter:")
    if ans == "s":
        spa_1 = "s"
    elif ans == "n":
        spa_2 = "n"
    elif ans == "o":
        spa_3 = "o"
    elif ans == "w":
        spa_4 = "w"
    else:
      wrong()
    print(spa_1,spa_2,spa_3,spa_4)