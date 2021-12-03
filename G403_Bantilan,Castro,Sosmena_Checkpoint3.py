print()
print("_____________________________________________")
print("Hello There!")
print("Welcome to CHB calculator")
print("_____________________________________________")
print()
print()
print("Input required numeric value")
print()


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("________________________________________")
print("Select operation.")
print("1. Initial Wall Area  ")
print("2. Total Wall Opening  ")
print("3. Total Wall Area ")
print("4. initial No. of CHB ")
print("5. Total No. of CHB")
print("6. Total Price of CHB for Wall No. 1")
print("7. Quit")
print("________________________________________")
print()
print("Note: \n ENTER NUMERIC VALUE ONLY!")
print()


try:
    sides = int(input("Wall Number:"))
    total = int(0)

except ValueError:
    print("No match! Please input numeric characters.")

while True:

    choice = input("Enter choice(1/2/3/4/5/6/7): ")  # take input from the user

    if choice in ('1', '2', '3', '4', '5', '6', '7'):  # check if choice is one of the options

        if choice == '1':
            num1 = float(input("Enter length of wall: "))
            num2 = float(input("Enter height of wall: "))
            print("Initial Wall Area" "=", multiply(num1, num2))
            print("")
            continue

        elif choice == '2':
            num1 = float(input("Enter length of opening: "))
            num2 = float(input("Enter width of opening: "))
            print("Total Wall Opening" "=", multiply(num1, num2))
            print("")

        elif choice == '3':
            num1 = float(input("Initial Wall Area: "))
            num2 = float(input("Total Wall opening: "))
            print("Total Wall Area", "=", subtract(num1, num2))
            print("")

        elif choice == '4':
            num1 = float(input("Total Wall Area: "))
            num2 = 12.5
            print("Initial No. of CHB", "=", multiply(num1, num2))
            print("")

        elif choice == '5':
            num1 = float(input("Initial No. of CHB: "))
            num2 = 10
            print("Total No. of CHB", "=", add(num1, num2))
            print("")

        elif choice == "6":
            num1 = float(input("Enter Price of single CHB: "))
            num2 = float(input("Enter Total No. of CHB: "))
            print("Total Price of CHB for Wall No. 1", "=", multiply(num1, num2))
            print("")
        elif choice == "7":
            print("Successfully exited in the CHB Calculator! Thank you.")
            break

        else:
            print("No match! Please input numeric characters.")
            break