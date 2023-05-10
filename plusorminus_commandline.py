"""Project Description: 
The Plus or Minus project is a simple number guessing game. 
The computer will generate a random number between 1 and 100 and the player must guess the number. 
The computer will give a hint if the guess is too high or too low until the correct number is guessed."""

from random import randint

def ask_number() :
    error = True
    while error == True :
        try : 
            toto = int(input())
        except ValueError :
            print ("Please write a number between 1 and 100 :")
        else :
            error = False
    return toto

answer = "Yes"

while answer == "Yes" :
    print("""Welcome to the Plus or Minus game.
You must guess the number between 1 and 100 the computer is thinking of.
Take a guess :""")
    nb_guess = 1
    x = randint(1,100)
    num = ask_number() 

    while num != x :
        if num > x :
            print ("Too bad, it's wrong. Try again, it is lower.")
        if num < x :
            print ("Too bad, it's wrong. Try again, it is higher.")
        num = ask_number()
        nb_guess = nb_guess + 1

    print (f"""You won in {nb_guess} guesses! The number the computer was thinking of is {num}. 
Play again? Yes/No""")
    answer = input()
