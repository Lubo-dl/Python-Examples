



import random
number = random.randint(1,10)
print("\nGuess Game!")
print("Guess Between 1 and 10.")
print("You Have Only 3 Lives!")

for i in range(0,3):
    userInput = int(input("Guess The Number!"))
    if userInput ==number:
        print("Wow! You Won!")
        print(f"You Guess The Right Number!")


