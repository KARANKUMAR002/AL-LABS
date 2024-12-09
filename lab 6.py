print("task no 1")
def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
print("The number of words in the sentence is:", count_words(sentence))


print("task no 2")
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
number = int(input("Enter a number: "))
print("The sum of the digits is:", sum_of_digits(number))




print("task no 3")
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter an integer: "))
print("The number is:", check_even_odd(number))