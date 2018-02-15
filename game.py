import re

from random import randint

def coin_flip():
    i = 0
    right = 0
    while i < 5:
        
        choise = input("Choose either heads or tails. ").lower()
        
        while not choise == "heads" and not choise == "tails" and not choise == "tales":
            choise = input('Sorry, I did not understand what you wrote! Please white "heads" or "tails". ').lower()
        
        if choise == "heads":
            choise = 1
        elif choise == "tails"  or choise == "tales":
            choise = 2
     
        coin = randint(1,2)
        if choise == coin:
            print ("You win!")
            right += 1
        else:
            print ("Unfortunately, you lose.")
        if coin == 1:
            print ("In a coin flip wins heads. \n")
        else:
            print ("In a coin flip wins tails. \n")
            
        i += 1
    if right >= 4:
        print(name + ", great result!" + str(right) + " out of 5!\n")
    elif right == 3:
        print(name + ", good result! 3 out of 5! \n")
    else:
        print(name + ", not the best result. Only " + str(right) +  " out of 5!\n")
    
        
def guess_number():
    opinion = int(input("I'm guessing a natural number less than 20. Guess which one! "))
    number = randint(1,19)
    attempt = 0

    while number != opinion:
        if number > opinion:
            print ("The number I'm guessing is bigger!")
        else:
            print ("The number I'm guessing is smaller!")
        attempt += 1
        opinion = int(input("Try again: "))
    if attempt == 0:
        print ("Correctly! You're just a clairvoyant! \n")
    elif attempt < 4:
        print ("Correctly! How could you have guessed so quickly?! \n")
    elif attempt < 6:
        print ("Correctly! \n")
    else:
        print("Now it's right. Although you could have guessed before! \n")
        
riddles = []
answers = []

def new_riddle(riddle, answer):
    riddles.append(riddle)
    answers.append(answer)

new_riddle("I have a head & no body, but I do have a tail. What am I? ", "coin")
new_riddle("I don't have wings, but I can fly. I don’t have eyes, but I can cry! What am I? ", "cloud")
new_riddle("If you are running in a race and pass the second place person, what place are you in? (Please answer with a number)", "2")
new_riddle("I know a word of letters three. Add two and fewer there will be. What is the word? ", "few")
new_riddle("There was a girl half my age when I was 12, now I am 64, how old is she? (Please answer with a number) ", "58")

def riddle_game():
    i = 0
    right = 0
    while i<5:
        print(riddles[i])
        user_answer = input().lower()
        if re.search(answers[i], user_answer):
            print("Correct!\n")
            right += 1
        else:
            print('Unfortunatelly, it is wrong. The right answer is "'  + str(answers[i]) + '"  \n')
        i += 1
    if right >= 4:
        print (name + ", You are a master of riddles! \n")
    elif right == 3 or right == 2:
        print (name + ", You are good at riddles! \n")
    else:
        print(name + ", solving riddles is clearly not your strong point! \n")
 
def game_choise():
    choise = input(name +", please choose the game: coin flip, guess the number or riddles. \n").lower()
    while not re.search("[coin, flip, guess, number, riddle]", choise):
        choise = input('Sorry, I did not understand what you wrote! Please type "coin flip" , "guess the number" or "riddles". \n').lower()
    if re.search("coin", choise) or re.search("flip", choise):
        coin_flip()
    elif re.search("guess", choise) or re.search("number", choise):
        guess_number()
    elif re.search("riddle", choise):
        riddle_game()   
    
name = input("Welcome to the game! What is your name? ")
game_choise()

while True: 
    again = input("Do you want to play more? (yes/no)").lower()

    while not re.search("[yes, no]", again):
        again = input('Sorry, I did not understand what you wrote! Please white "yes" or "no". ').lower()

    if re.search("yes", again):
        game_choise()
    elif re.search("no", again):
        print("Buy, " + name + "! Hope to see you soon!")
        break

    



    
 
    
