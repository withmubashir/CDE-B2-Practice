# print("Name: Mubashir Hussain\nFather Name: Muhammad Saleh\nDate of Birth: 10\\03\\2009")

# bio = [
#     "Name: Mubashir Hussain",
#     "F. Name Muhammad Saleh",
#     "Education: Intermediate",
#     "Center: SMIT Zaitoon Ashraf",
#     "Roll Number: 371381"
# ]

# print(bio)

# num = 88
# print(num + 20)
# print(num -20)
# print(num/20)
# print(num*20)
# print(num**2)
# num+=20
# num-=20
# num*=20
# num/=20
# print(num)

# english = 55
# islamiat = 67
# math = 100

# total_marks = 300

# numbers = english+islamiat+math
# print(numbers/total_marks*100)

# service_year = int(input("enter your years service " ))
# salary = int(input("enter your salary" ))
# if service_year >= 5:
#     bonus = int(salary/20)
#     print("Conratulations! You Got a Bonus of:", bonus)
# else:
#     print("Sorry, you are not eligible for a bonus.")

# age = int(input("Enter Your Age"))

# if age > 17:
#     print("You're Eligible For Voting")
# else:
#     print("You Are Not Eligible For Voting")
# marks = int(input("Enter your Marks"))

# if marks > 80 and marks <= 100:
#     print("Grade A")
# elif marks > 60 and marks <= 80:
#     print("Grade B")
# elif marks > 50 and marks <= 60:
#     print("Grade C")
# elif marks > 45 and marks <= 50:
#     print("Grade D")
# elif marks > 25 and marks <= 45:
#     print("Grade E")
# elif marks > 0 and marks <= 25:
#     print("Grade F")
# else:
# #     print("Invalid Input")

# number = int(input("Write a Number: "))
# remainder = number%2

# if remainder == 0:
#     print("This is an Even Number")
# else:
#     print("This is an Odd Number")

# number1 = int(input("Write a Number: "))
# remainder1 = number1%7

# if remainder1 == 0:
#     print("This number is divisible by 7")
# else:
#     print("This is not divisible by 7")


# number3 = int(input("Enter a number: "))

# if number3%5 == 0:
#     print("Hello")
# else:
#     print("Bye")

# shape_input = int(input("Enter the length: "))
# shape_input2 = int(input("Enter the breadth: "))

# if shape_input == shape_input2:
#     print("it's a squre shape")
# else:
#     print("it's a rectangle shape")

# input_value = int(input("Enter the number: "))
# input_value2 = int(input("Enter the 2nd number : "))

# if input_value > input_value2:
#     print("input one is greator ", input_value )
# else:
#     print("input two is greator ", input_value2)

print("Our Product Price is 100")
input_quantity = int(input("Enter Your Product Quantity: "))
total_price = input_quantity*100
discount_price = total_price - total_price/10
if total_price >= 1000:
    print("Your total cost is after 10% discount:", int(discount_price))
else:
    print("you are not eligible for discount")
