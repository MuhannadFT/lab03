def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(number)
