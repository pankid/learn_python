from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!


while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    
  
    if guess == random_number:
        print "You Win!"
        break
    elif guess < 1 or guess > 10 :
        print "try again"
        
    elif guess != random_number: 
        print "you have %s guesses left" % (guesses_left)
        guesses_left = guesses_left - 1
else: 
    print "You Lose"
    

