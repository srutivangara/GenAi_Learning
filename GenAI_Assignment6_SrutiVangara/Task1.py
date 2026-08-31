try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))

    result = num / den

except ValueError:
    print("Invalid input. Please enter numbers.")

except ZeroDivisionError:
    print("Denominator cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")