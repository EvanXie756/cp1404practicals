"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
The value error will occur when both the numerator and denominator are not a vaild number
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the fraction cannot divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
