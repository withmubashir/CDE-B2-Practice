#Comparison Operators
print(45 != 54) 
print(True and False) #and
print(True or False) #or

#List adding and changing elements
countries = [
    "Pakistan",
    "China",
    "Afghanistan"
]

print(type(countries))

print(countries[0])
print(countries[2])
print(countries[1])

countries.append("India")

print(countries)

countries.insert(0, "South Korea")

print(countries)

countries[2] = "Italy"

print(countries)

#Lists: Taking Slice out of them

print(countries[1:4])

print(countries[:3])

print(countries[2:])

#print using negative index

print(countries[-4:-1])

print(countries[-5:-2])

print(countries[-3:])