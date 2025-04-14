# 1 WAP to check if a number entered by uder is odd or even.

i = int(input("Enter any Number: "))
if(i%2==0):
    print(i, "is an even number.")
else:
    print(i, "is an odd number.")

# 2 WAP to find the greatest of 3 number entered by the user.

u_input1 = int(input("Enter any Number: "))
u_input2 = int(input("Enter any Number: "))
u_input3 = int(input("Enter any Number: "))

if(u_input1 > u_input2 and u_input1 > u_input3):
    print(u_input1, "is the greatest number")
elif(u_input2 > u_input1 and u_input2 > u_input3):
    print(u_input2, "is the greatest number")
else:
    print(u_input3, "is the greatest number")

# WAP to check if a number is multiple of 7 or NOT

u_input = int(input("Enter any Number: "))

if(u_input%7==0):
    print(u_input, "is multiple of 7")
else:
    print(u_input, "is NOT multiple of 7")