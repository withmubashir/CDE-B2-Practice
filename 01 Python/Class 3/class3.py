cities=["Karachi", "Islamabad", "Lahore"]

for temp in range(len(cities)):
    print(temp)

for temp1 in cities:
    print(f"{temp1} index value is {temp1}")

for temp2 in [[1,2,3], ["a","b","c"],["@","#","$"]]:
    print(temp2)


bio_data_dic={
    "first_name" : "Mubashir Hussain",
    "last_name" : "Saleh",
    "age" : "12",
    "weight" : "9" 
}

for key, value in bio_data_dic.items():
    print(f"Key {key} have value {value} ")
