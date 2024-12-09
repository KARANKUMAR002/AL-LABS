print("task no 1")
class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car Info:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles

# Create a Car object with predefined details
car = Car("Toyota", "Corolla", 2020, 15000)

# Display initial car information
car.display_info()

# Ask the user for miles to drive
miles_to_drive = int(input("Enter miles to drive: "))

# Drive the car and update mileage
car.drive(miles_to_drive)

# Display the updated car information
car.display_info()





print("task no 2")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def average_marks(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Average Marks: {self.average_marks():.2f}")

# Example usage
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))

student = Student(name, age)

marks = list(map(int, input("Enter the student's marks (separated by spaces): ").split()))
student.add_marks(marks)

student.display_info()





print("task no 3")
class BankAccount:
    def __init__(self, account_holder, balance=0):
         
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
         
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        
        print(f"Current balance: {self.balance}")

# Function to get user input and create an account
def main():
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input(f"Enter the initial balance for {account_holder}: "))

    # Create the BankAccount object
    account = BankAccount(account_holder, initial_balance)
    
    # Display current balance
    account.display_balance()

    # Ask user for deposit amount
    deposit_amount = float(input("Enter the deposit amount: "))
    account.deposit(deposit_amount)

    # Ask user for withdrawal amount
    withdraw_amount = float(input("Enter the withdrawal amount: "))
    account.withdraw(withdraw_amount)

    # Display final balance
    account.display_balance()

if __name__ == "__main__":
    main()
