#Create a user input list and let the user input 5 numbers, Create another list in which you have to display the sum of digit of the numbers entered by the user


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

user_numbers = []

for _ in range(5):
    while True:
        try:
           
            user_input = int(input("Enter a number: "))
            
            user_numbers.append(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


sum_of_digits_list = [sum_of_digits(num) for num in user_numbers]


print("Original list of numbers:", user_numbers)
print("List of sums of digits:", sum_of_digits_list)
