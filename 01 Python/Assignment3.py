vowels = "aeiouAEIOU"
user_input = input("Enter a string: ")
vowel_count = 0

for letter in user_input:
    if letter in vowels:
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)