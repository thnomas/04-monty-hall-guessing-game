import random

# randomly assign correct door
correct_num = random.randint(1, 3)
# print(f"the correct door is: {correct_num}")

print("+---------------------------------------------------------------------------------------+")
print("+ Welcome!")
print("+ Play to win a brand new luxury sports car. All you have to do is pick the right door.")

# take users guess
print('+ Pick a door (number between 1-3): ')
guess = int(input())

li = [1, 2, 3]
li.remove(correct_num)

if guess in li:
    li.remove(guess)
else:
    li.remove(random.choice(li))

# print(li)

print(f"You've picked door #{guess}. I can tell you that the car is not behind door #{li[0]}.")
print(f"Would you like to keep your original guess or change your guess (Enter number: ) ")
guess = int(input())

if guess == correct_num:
    print("Congrats! You've won a brand new sports car!")
else:
    print(f"I'm sorry, you've lost! The correct answer was door #{correct_num}")

