# Palindrome Checker
# Take a string from the user
# Check whether it is a palindrome or not
# (A palindrome reads the same forward and backward, e.g. “madam”, “level”)

txt = str(input("Enter word to check if it is palindrom: ")).lower()

txt1 = txt[::-1]

if txt == txt1:
    print("Your word is Palindrom")
else:
    print("not palindrom")