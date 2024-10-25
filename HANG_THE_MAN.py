#HANG MAN by Aaron, and Tate, and Martin, and Amon
import random
#make all the variables/list: Everyone
Wrong_count = 0
spa_0 = "_"
spa_1 = "_"
spa_2 = "_"
spa_3 = "_"    
words = ["snow", "wolf", "moon", "star", "lamp", "bruh", "sing", "rice", "tree", "keep", "dark", "aron", "sans", "wine", "volk", "sing", "sins","bean", "rugs", "tape", "bait", "dead","kind", "thin", "song", "road", "read", "quit", "race"] 
word = random.choice(words)
#Function for winning, and add or not add a body part depending on the letter chosen:Aaron Shelby and Tate Morgan
def win():
   return f"Congrats, you get ඞamongiඞ !"
def wrong():
    global Wrong_count
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
    for i in range(1):
        if Wrong_count == 1:
            Layer_5 = head + Layer_5
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            return Layer_5
        elif Wrong_count == 2:
            Layer_5 = head + Layer_5
            Layer_4 = body + Layer_4
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            return Layer_4
        elif Wrong_count == 3:
            Layer_5 = head + Layer_5
            Layer_4 = Larm + body + Layer_4
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            return Layer_4
        elif Wrong_count == 4:
            Layer_5 = head + Layer_5
            Layer_4 = Larm + body + Rarm + Layer_4
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            return Layer_4
        elif Wrong_count == 5:
            Layer_5 = head + Layer_5
            Layer_4 = Larm + body + Rarm + Layer_4 
            Layer_3 = Lleg + Layer_3
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            return Layer_3
        elif Wrong_count == 6:
            Layer_5 = head + Layer_5
            Layer_4 = Larm + body + Rarm + Layer_4 
            Layer_3 = Lleg + Rleg + Layer_3
            print(Layer_7)
            print(Layer_6)
            print(Layer_5)
            print(Layer_4)
            print(Layer_3)
            print(Layer_2)
            print(Layer_1)
            return 
        else: 
            print("Congratulations, your a failure ඞ")
            print("The word was", word)
#Make a guess: Amon Dipp and loop the guesses: Martin Labarca
while True:
    ans = input("Tell a letter:")
    if ans == word[0]:
        spa_0 = word[0]
    elif ans == word[1]:
        spa_1 = word[1]
    elif ans == word[2]:
        spa_2 = word[2]
    elif ans == word[3]:
        spa_3 = word[3]
    else:
      Wrong_count = Wrong_count + 1
      wrong()
    print(spa_0,spa_1,spa_2,spa_3)
    if spa_0== word[0] and spa_1== word[1] and spa_2== word[2] and spa_3== word[3]:
      print(win())