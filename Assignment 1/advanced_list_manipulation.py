# Use input to get a list of comma-separated numbers
numbers_input = input("Enter a list of numbers separated by commas: ")
numbers = [int(num) for num in numbers_input.split(',')]
# Function to find the sum of the numbers
def find_sum(numbers):
    return sum(numbers)

# Function to find the average of the numbers
def find_average(numbers):
    return sum(numbers) / len(numbers)

# Function to find the maximum of the numbers
def find_maximum(numbers):
    return max(numbers)

# Function to find the minimum of the numbers
def find_minimum(numbers):
    return min(numbers)

# Function to filter out even numbers
def filter_even(numbers):
    return [num for num in numbers if num % 2 != 0]
# Test the functions
sum_result = find_sum(numbers)
average_result = find_average(numbers)
maximum_result = find_maximum(numbers)
minimum_result = find_minimum(numbers)
filtered_numbers = filter_even(numbers)

print("Sum:", sum_result)
print("Average:", average_result)
print("Maximum:", maximum_result)
print("Minimum:", minimum_result)
print("Filtered Even Numbers:", filtered_numbers)
