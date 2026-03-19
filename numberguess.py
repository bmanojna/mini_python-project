# number guessing game.py

import random
number = random.randint(1,10)
while True:
    guess = (int(input("enter a guess: ")))
if guess == number:
    print("correct")
elif guess > number:
    print("too high")
else:
    print("too low")

    attempts += 1
    if attempts == 5:
      print("Game Over 😢")
         