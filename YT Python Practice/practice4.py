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