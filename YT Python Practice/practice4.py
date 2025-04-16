#Store following word meanings in a python dictionary :
#table : “a piece of furniture”,“list of facts & figures”
#cat : “a small animal”

dict = {
    "table"  : ("a piece of furniture","list of facts & figures"),
    "cat" : "a small anima"
    }

print(type(dict["table"]))

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students. 
# ”python” , “java” , “C++” , “python” , “javascript” , “java” , “python” , “java” , “C++” , “C”

subjects = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}

print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

dict2 = {}

dict2 ["Physics"] =  int(input("Enter Marks: "))
dict2 ["Math"] =  int(input("Enter Marks: "))
dict2 ["Urdu"] =  int(input("Enter Marks: "))

print(dict2)

dict3 = {}
x = int(input("Enter Marks: "))
dict3.update( {"Physics" : x} )
x = int(input("Enter Marks: "))
dict3.update( {"Math" : x} )
x = int(input("Enter Marks: "))
dict3.update( {"Urdu" : x} )

print(dict3)