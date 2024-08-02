# @TODO: Write a for loop function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))




#without for loop
randomlist = [1,2,3,4,5]

def averafe(numbers):
    total = sum(numbers)/len(numbers)
    return total

average(randomlist)
def average(numbers):
#finding the total count - len
    total count = len(numbers)
    total_sum = 0
    for sum in numbers:
        total_sum += sum
    result = total_sum/total_count
    return result