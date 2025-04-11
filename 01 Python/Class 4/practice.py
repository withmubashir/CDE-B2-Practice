dictionaries = {'first_name' : 'Mubashir Hussain',
                'last_name' : 'Saleh',
                'age' : 15,
                'weight' : 30,}

print(dictionaries)

dictionaries['profession'] = 'Cloud Data Engineer'

print(dictionaries)

bio_data_dict = [
    {
       'first_name': 'Qasim',
       'last_name': 'Hassan',
       'age': 15,
       'weight': 75,
       'profession': 'Data Engineer',
       'phone number': ['246846', '32546946'] 
    },
    {
       'first_name': 'Uzair',
       'last_name': 'Khan',
       'age': 20,
       'weight': 55,
       'profession': 'Data Engineer',
       'phone number': ['24677846', '3022546946'] 
    },
    {
       'first_name': 'Ayan',
       'last_name': 'Hussain',
       'age': 55,
       'weight': 15,
       'profession': 'Data Engineer',
       'phone number': ['2446', '32946'] 
    }
]
print(bio_data_dict) 

#functions with parameter
def new(num): 
    print(num**3)

new(28)

#functions without parameter
def new1():
    print("Hi!")

new1()

#function with default values

def abc(num, num1):
    print(3*4/num**num1)
abc(2,3)

#function with returning values

def add(num1=0, num2=0, num3=0):
    return num1+num2+num3
print(add)