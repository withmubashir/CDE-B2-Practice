vowels = set("aeiouAEIOU")
user_input = input("Enter a string: ")
vowel_count = sum(1 for _ in user_input if _ in vowels)
print(f"Number of vowels in the string: {vowel_count}")