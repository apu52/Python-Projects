def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def convert_number():
    print("Choose the base conversion:")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        decimal = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal)}")
    elif choice == '2':
        decimal = int(input("Enter a decimal number: "))
        print(f"Octal: {decimal_to_octal(decimal)}")
    elif choice == '3':
        decimal = int(input("Enter a decimal number: "))
        print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
    elif choice == '4':
        binary = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary)}")
    elif choice == '5':
        octal = input("Enter an octal number: ")
        print(f"Decimal: {octal_to_decimal(octal)}")
    elif choice == '6':
        hexadecimal = input("Enter a hexadecimal number: ")
        print(f"Decimal: {hexadecimal_to_decimal(hexadecimal)}")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    while True:
        convert_number()
        another = input("Do you want to convert another number? (yes/no): ")
        if another.lower() != 'yes':
            break
