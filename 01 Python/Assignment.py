print("Name: Mubashir Hussain\nFather Name: Muhammad Saleh\nDate of Birth: 10\\03\\2009")

bio = [
    "Name: Mubashir Hussain",
    "F. Name Muhammad Saleh",
    "Education: Intermediate",
    "Center: SMIT Zaitoon Ashraf",
    "Roll Number: 371381"
]

print(bio)

num = 88
print(num + 20)
print(num -20)
print(num/20)
print(num*20)
print(num**2)
num+=20
num-=20
num*=20
num/=20
print(num)

english = 55
islamiat = 67
math = 100

total_marks = 300

numbers = english+islamiat+math
print(numbers/total_marks*100)

service_year = int(input("enter your years service " ))
salary = int(input("enter your salary" ))
if service_year >= 5:
    bonus = int(salary/20)
    print("Conratulations! You Got a Bonus of:", bonus)
else:
    print("Sorry, you are not eligible for a bonus.")

age = int(input("Enter Your Age"))

if age > 17:
    print("You're Eligible For Voting")
else:
    print("You Are Not Eligible For Voting")
