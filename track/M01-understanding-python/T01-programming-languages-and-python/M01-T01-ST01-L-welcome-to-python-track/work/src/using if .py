mark = int (input())
attand = int (input())
project = input ()

if mark <= 100 and attand <= 100:
    if project == "yes":
        print("Eligible")
    else:
        print("not eligible")
else:
    print("not eligible")