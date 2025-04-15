#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

lists = []
input1 = input("Enter any Movie Name: ")
input2 = input("Enter any Movie Name: ")
input3 = input("Enter any Movie Name: ")

lists.append(input1)
lists.append(input2)
lists.append(input3)

print(lists)

#WAP to check if a list contains a palindrome of elements. 

list2 = ["m","a","p","m"]

new = list2.copy()
new.reverse()
if( new == list2):
    print(list2, "is palindrome")
else:
    print(list2, "is NOT palindrome")


#WAP to count the number of students with the “A” grade in the following tuple.

tup = ("A","B","C","B","A","F","E","A","A","B","C","B","A","F","E","A","A","B","C","B","A","F","E","A")

print(tup.count("A"))


