# Modules
import os
import csv

# Prompt user for title lookup
book = str(input ("What title are you loking for?"))

# Set path for file
csvpath = os.path.join("..", "Resources", "comic_books.csv")

# Set variable to check if we found the video
found = False

# Open the CSV using the UTF-8 encoding
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    # Loop through looking for the video
for row in cvsreader:
        if book in row [0]:
              print(row[0] + " was published by " + row [8] + " in" + row[9])
            # Set variable to confirm we have found the video
            found = True
        
    # If the book is never found, alert the user
    if found is False
        print("Sorry about this, we dont seem to have what you are looking for!")
