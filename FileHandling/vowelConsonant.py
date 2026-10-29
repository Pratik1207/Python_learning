# Count Vowels and Consonants
# Take a string from the user
# Count how many vowels and consonants are present
# Print both counts

txt = str(input("Enter a sentence: "))

sentence = txt.lower()

vowel = 0
cons = 0

for x in sentence:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        vowel = vowel + 1
    elif x.isalpha():
        cons = cons+1

print(f"Total number of vowel is: {vowel} and consonants is: {cons}")