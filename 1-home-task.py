entered_word = input("enter word").strip()
reversed_word = entered_word[::-1]
print(reversed_word)
if entered_word == reversed_word:
    print("+")
else:
    print("-")