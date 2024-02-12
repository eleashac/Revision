""" This program asks the user to input two numbers. It then outputs the largest
 number, or states equal. The program repeats until zero is entered"""

# create loop until zero is entered
while True:

    # get user input number
    num1 = int(input("Choose your first number: "))
    if num1 == 0:
        break
    else:
        num2 = int(input("Choose your second number: "))

    if num1 > num2:
        print(f"{num1} is bigger")
        print("Input 0 to end")
        print()

    elif num2 > num1:
        print(f"{num2} is bigger")
        print("Input 0 to end")
        print()

    else:
        print("These numbers are equal")
        print("Input 0 to end")
        print()
