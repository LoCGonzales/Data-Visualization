# The list of candies to print to the screen
candy_list = [
    "Snickers", 
    "Kit Kat", 
    "Sour Patch Kids", 
    "Juicy Fruit", 
    "Swedish Fish", 
    "Skittles", 
    "Hershey Bar", 
    "Starbursts", 
    "M&Ms"
    ]
candy_list[0]
# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    index_of_candy = candy_list.index(candy)
    Index_of_candy_str = str(index_of_candy)
    print(f'[{index_of_candy_str}] {candy}')
    
# Run through a loop which allows the user to choose which candies to take home with them
print("Which candy would you like to bring home?")
for # YOUR CODE HERE:
    selected = input("Input the number of the candy you want: ")

    # Add the candy at the index chosen to the candy_cart list
    # YOUR CODE HERE

# Loop through the candy_cart to say what candies were brought home
print("I brought home with me...")
for # YOUR CODE HERE
    print(candy)