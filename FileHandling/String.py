# String Methods Practice
# Take a sentence from the user
# Convert it to uppercase and lowercase
# Remove extra spaces using strip()
# Split the sentence into words
# Replace any one word with another word
# Print the results

sentnece = str(input("Enter a Sentence: "))

print("Your sentence in upper case: ", sentnece.upper())

print("Your sentence in lower case: ", sentnece.lower())

print("Your sentence without any extra space: ", sentnece.strip())

print("Each words of your sentence is: ", sentnece.split())

print(sentnece.replace("a", "b"))