from random import randint
name=input("What is your name? ")
num=randint(1,100)

print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess is. What number do you think it is?")

for i in range(8):
  guess=int(input("What is your first guess?"))
  if guess == num:
    print(f"CONGRATULATIONS YOU WIN, it took you {i+1} tries")
    break
  elif (guess < 1 and guess > 100):
    print("You have chosen a number that is out of play")
  elif guess < num:
    print("You are wrong, and you are lower than the number")
  elif guess > num:
    print("You are wrong, and you are higher than the number")
  else:
    print("Choose a new number and try again")
  