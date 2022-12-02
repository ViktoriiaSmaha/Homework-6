entered_text = input("Enter string").strip()
if entered_text.startswith("abc"):
    print(entered_text.replace("abc", "www"))
else:
    print(entered_text + "zzz")