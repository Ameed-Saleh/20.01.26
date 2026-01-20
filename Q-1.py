base = float(input('Enter base: '))
height = float(input('Enter height: '))
while base <= 0 or height <= 0:

    if base > 0 :
        base = base
    else:
        base = float(input('Enter base: '))
    if height > 0 :
        height = height
    else:
        height = float(input('Enter height: '))

else :
    print("area =", (base * height)/2 )