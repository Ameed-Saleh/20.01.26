a = float(input("Enter a slide 1: "))
b = float(input("Enter a slide 2: "))
c = float(input("Enter a slide 3: "))
if a == b == c :
    print("משולש שווה צלעות")
else :
    if a == b or a == c or b == c:
      print("משולש שווה שוקיים")
    else:
      print("אינו משןלש מיוחד לצערי הרב")