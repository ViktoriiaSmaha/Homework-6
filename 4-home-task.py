entered_text = input("Enter text")
result = ""

for letter in entered_text:
    if letter.isalpha():
        result = result + letter

print(result)