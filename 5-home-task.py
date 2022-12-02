your_mail = input("Enter mail")

if your_mail.find("@") != -1 and your_mail.find(".") != -1:
    print('yes')
else:
    print('no')