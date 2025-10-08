import random
for i in range(1,11):
   guess = int(input("Guess a number between 1 and 11: "))

   if guess == number:
      print("Correct!")
   else:
      print(f"Wrong! The number was {number}")
