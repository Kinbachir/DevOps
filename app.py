def calculate_pgcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calculate_ppm(a, b):
    return abs(a * b) // calculate_pgcd(a, b)


def main():
    try:

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        pgcd = calculate_pgcd(num1, num2)
        ppm = calculate_ppm(num1, num2)
        
        print(f"PGCD (GCD) of {num1} and {num2} is: {pgcd}")
        print(f"PPM (LCM) of {num1} and {num2} is: {ppm}")

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
