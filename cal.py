import mymath

while True:
    
    try:
        chose = int(input("Choose operation (1-add, 2-sub): "))
        num1, num2 = float(input("enter the first number: ")), float(input("enter the second number: "))

        if chose == 1:
            print(mymath.add(num1,num2))
        elif chose == 2:
            print(mymath.sub(num1,num2))
        else:
            print("wrong number")

    except ValueError:
        print("chose the right number")
        continue

    agin = input("do you want try agin? ")

    if agin == "no":
        print("have a nice day!")
        break