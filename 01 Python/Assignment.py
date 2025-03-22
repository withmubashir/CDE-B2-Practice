# # 1. Print Your Name with your Father name and Date of birth using suitable escape sequence charactor

# print("Name: Mubashir Hussain\nFather Name: Muhammad Saleh\nDate of Birth: 10\\03\\2009")

# # 2. Write your small bio using variables and print it using print function

# bio = [
#     "Name: Mubashir Hussain",
#     "F. Name Muhammad Saleh",
#     "Education: Intermediate",
#     "Center: SMIT Zaitoon Ashraf",
#     "Roll Number: 371381"
# ]

# print(bio)

# # 3. Write a program in which use all the operators we can use in Python

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

# # 4. Completes the following steps of small task:
# #     - Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
# #     - Mention Variable of Total Marks and assign 300 to it
# #     - Calculate Percentage

# english = 55
# islamiat = 67
# math = 100

# total_marks = 300

# numbers = english+islamiat+math
# print(numbers/total_marks*100)

# # 1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# # Ask user for their salary and year of service and print the net bonus amount.

# service_year = int(input("enter your years service " ))
# salary = int(input("enter your salary" ))
# if service_year >= 5:
#     bonus = int(salary/20)
#     print("Conratulations! You Got a Bonus of:", bonus)
# else:
#     print("Sorry, you are not eligible for a bonus.")


# # 2) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

# age = int(input("Enter Your Age"))

# if age > 17:
#     print("You're Eligible For Voting")
# else:
#     print("You Are Not Eligible For Voting")

# # 3) Write a program to check whether a number entered by user is even or odd.

# number = int(input("Write a Number: "))
# remainder = number%2

# if remainder == 0:
#     print("This is an Even Number")
# else:
#     print("This is an Odd Number")

# # 4) Write a program to check whether a number is divisible by 7 or not. Show Answer

# number1 = int(input("Write a Number: "))
# remainder1 = number1%7

# if remainder1 == 0:
#     print("This number is divisible by 7")
# else:
#     print("This is not divisible by 7")

# # 5) Write a program to display 
# # "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

# number3 = int(input("Enter a number: "))

# if number3%5 == 0:
#     print("Hello")
# else:
#     print("Bye")

# # 9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

# shape_input = int(input("Enter the length: "))
# shape_input2 = int(input("Enter the breadth: "))

# if shape_input == shape_input2:
#     print("it's a squre shape")
# else:
#     print("it's a rectangle shape")

# # 10) Take two int values from user and print greatest among them.

# input_value = int(input("Enter the number: "))
# input_value2 = int(input("Enter the 2nd number : "))

# if input_value > input_value2:
#     print("input one is greator ", input_value )
# else:
#     print("input two is greator ", input_value2)

# # 11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# # Ask user for quantity
# # Suppose, one unit will cost 100.
# # Judge and print total cost for user.

# print("Our Product Price is 100")
# input_quantity = int(input("Enter Your Product Quantity: "))
# total_price = input_quantity*100
# discount_price = total_price - total_price/10
# if total_price >= 1000:
#     print("Your total cost is after 10% discount:", int(discount_price))
# else:
#     print("you are not eligible for discount")

# # 12) A school has following rules for grading system:
# # a. Below 25 - F
# # b. 25 to 45 - E
# # c. 45 to 50 - D
# # d. 50 to 60 - C
# # e. 60 to 80 - B
# # f. Above 80 - A
# # Ask user to enter marks and print the corresponding grade.

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
#     print("Invalid Input")


# # 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# # Take following input from user
# # - Number of classes held
# # - Number of classes attended.
# # And print
# # - percentage of class attended
# # - Is student is allowed to sit in exam or not.


# classes_attended = int(input("Enter the Numbers Of Classes Attended"))
# classes_held = int(input("Enter the Numbers Of Classes Held"))
# total_class = int((classes_attended / classes_held) * 100)

# if total_class >= 75:
#     print("You are allowed to sit in exam")
# else:
#     print("You are not allowed to sit in exam")

# 15) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# classes_attended1 = int(input("Enter the Numbers Of Classes Attended: "))
# classes_held1 = int(input("Enter the Numbers Of Classes Held: "))
# total_class1 = int((classes_attended1 / classes_held1) * 100)

# if total_class1 >= 75:
#     print("You are allowed to sit in exam")
# else:
#     cause = input("medical cause? 'Y' or 'N': ")
#     if cause == "Y": print("You are allowed to sit in exam")
#     else:print("You are not allowed to sit in exam")

# Write a program to display the last digit of a number.
# number4 = int(input("Enter any numbers: "))
# last_digit = number4%10
# print(f'Your last digit is: {last_digit}')

# 6) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#      Unit                                                     Price  
# uptp 100 units                                             no charge
# Next 200 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs.3500
# (For example if input unit is 97 than total bill amount is Rs.0
# (For example if input unit is 150 than total bill amount is Rs.750

# units = int(input("Enter Your Units: "))
# if units >=0 and units <=100:
#     print("Total bill amount is Rs.0")
# elif units >=101 and units <=200:
#     print(f"Total bill amount is Rs.{int(units*5)}")
# else:
#     print(f"Total bill amount is Rs.{int(units*10)}")

# 16) Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
# year = int(input("Enter any Year: "))
# new = 0
# if year == 1900 or year == 2000 or year == 2100:
#     new = year%400
#     if new == 0: print("it is leap year")
#     else:print("it is not leap year")
# else:
#     new = year%4
#     if new == 0: print("it is leap year")
#     else:print("it is not leap year")

# 13) Take input of age of 3 people by user and determine oldest and youngest among them.

age_1 = int(input("Enter Your Age: "))
age_2 = int(input("Enter Your Age: "))
age_3 = int(input("Enter Your Age: "))

if age_1 >= age_2 and age_1 >= age_3:
    oldest_age = age_1
elif age_2 >= age_1 and age_2 >= age_3:
    oldest_age = age_2
else:
    oldest_age = age_3

if age_1 <= age_2 and age_1 <= age_3:
    youngest_age = age_1
elif age_2 <= age_1 and age_2 <= age_3:
    youngest_age = age_2
else:
    youngest_age = age_3

print(f"the oldest age is {oldest_age}")
print(f"the youngest age is {youngest_age}")