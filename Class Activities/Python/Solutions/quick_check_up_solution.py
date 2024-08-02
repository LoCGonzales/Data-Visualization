import random 

numbers = [0,5,6,10]
random_number = random.choice(numbers)
print(f"The random number is:{random_number}")

# Print Hello User!
print("Hello User!")

# Take in User Input
name = input("What is your name? ")

# Respond Back with User Input
print("Hi " + name + "!")

# Take in the User Favorite Number
favorite_number = input("What is your favorite number? ")

# Respond Back with a statement based on your favorite number
if (int(favorite_number) < random_number):
    print("Your favorite number is lower than mine.")

elif (int(favorite_number) == random_number):
    print("Your favorite number is the same as mine!")

else:
    print("Your favorite number is higher than mine.")
