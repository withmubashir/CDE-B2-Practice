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

service_year = int(input("enter your service time" ))
salary = int(input("enter your salary" ))
if service_year >= 5:
    print(int(salary/20))
else:
    print("your service must equal or more than 5 year")