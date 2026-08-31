def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        print("Error: Factorial does not exist for negative numbers.")
    else:
        return  n * factorial(n - 1)

for num in [5, 0, -3]:
    print(f"Factorial of {num} is: {factorial(num)}")
