# 1. ADDITION
# 2. SUBTRACTION
# 3. MULTIPLICATION
# 4. DIVISION
# 5. AREA OF A TRIANGLE
# 6. SQUARE ROOT
# 7. EXPONENTIATION
# 8. EXPONENTIATION 3
# 9. EXPONENTIATION 4


from math import sqrt

operations = (input("do you want to perform a mathematical operation?: "))
print(" ")

if operations == "yes":

    print("OPERATIONS")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. DIVISION")
    print("4. MULTIPLICATION")
    print("5. FIND THE AREA OF A TRIANGLE")
    print("6. FIND SQUARE ROOT")
    print("7. EXPONENTIATION")
    print("8. EXPONENTIATION 3 ")
    print("9. EXPONENTIATION 4 ")
    print(" ")
    operation = int(input("select an operation to perform: "))

    while operation < 10:

        # The addition operation
        if operation == 1:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
            sums = float(num1 + num2 + num3)
            print("The sum of ", num1, num2, "and", num3, " = ", sums)

        # The Subtraction operation
        elif operation == 2:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            sub = float(num1 - num2)
            print("The difference of ", num1, " and ", num2, " = ", sub)

        # The division operation
        elif operation == 3:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            div = float(num1 / num2)
            print("The division of ", num1, " by ", num2, " = ", div)

        # The multiplication operation
        elif operation == 4:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            mul = float(num1 * num2)
            print("The product of ", num1, " and ", num2, " = ", mul)

        # The operation for finding the area of a triangle operation
        elif operation == 5:
            print(" ")
            num1 = int(input("Enter the base number: "))
            num2 = int(input("Enter the height number: "))
            AOT = float(num1 * num2 / 2)
            print("The area of triangle base ", num1, "and height ", num2, " = ", AOT)

        # The operation for finding the square root of a constant
        elif operation == 6:
            print(" ")
            num1 = int(input("Enter the number you want to find the square root of: "))
            root = float(sqrt(num1))
            print("\u221A", num1, "=", root)

        # The operation for finding the power of a constant
        elif operation == 7:
            print(" ")
            num1 = int(input("Enter the number you want to exponential: "))
            power = float(pow(num1, 2))
            print(num1, "\u00B2 = ", power)

        elif operation == 8:
            print(" ")
            num1 = int(input("Enter the number you want to exponential: "))
            power = float(pow(num1, 3))
            print("\u00B3", num1, "= ", power)

        elif operation == 9:
            print(" ")
            num1 = int(input("Enter the number you want to exponential: "))
            power = float(pow(num1, 4))
            print(num1, "\u2074 = ", power)

        else:
            print(" ")
            print("invalid Entry")
            print(" ")
            print(" ")
    operation += 1

elif operations == "no":
    print(" ")
    print("Thank you for visiting...")

else:
    print(" ")
    print("You have entered an invalid input")
    