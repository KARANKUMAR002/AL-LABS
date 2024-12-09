print("task no 1")
def draw_square(side_length):
    if side_length <= 0:
        print("Side length must be a positive integer.")
        return
    
    for _ in range(side_length):
        print("* " * side_length)

# Example usage
side_length = int(input("Enter the side length of the square: "))
draw_square(side_length)

print("task no 2")
def sum_of_even_numbers(numbers):
   
 # Use a list comprehension to filter even numbers and sum them
    return sum(number for number in numbers if number % 2 == 0)

# Ask the user for input
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("The sum of the even numbers is:", sum_of_even_numbers(numbers))






print("task no 3")
def countdown_to_zero(number):
    while number >= 0:
        print(number)
        number -= 1

# Ask the user for input
number = int(input("Enter a number to start the countdown: "))
countdown_to_zero(number)
