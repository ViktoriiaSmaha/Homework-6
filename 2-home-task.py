entered_text = input("Enter text")
entered_word = input("Enter word")
index = entered_text.find(entered_word)
if index  == -1:
    print("no")
else:
    print("yes")