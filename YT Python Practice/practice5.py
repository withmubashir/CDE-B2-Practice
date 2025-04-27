#Print numbers from 1 to 100.

a = 1
while a <=100:
    print(a)
    a+=1

#Print numbers from 100 to 1.

b = 100
while b>=1:
    print(b)
    b-=1

#Print the multiplication table of a number n.

i =1
n = int(input("Enter any Number: "))
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i +=1

nums = [1, 4, 6, 9, 16, 25, 36, 49, 64, 81, 100]

c = 0
while c <= len(nums)-1:
    print(nums[c])

    c+=1

#Search for a number x in this tuple using loop:

e = int(input("Enter any number: "))
x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
d = 0
while d<len(x):
    if(x[d]==e):
        print("found!" )
    d+=1