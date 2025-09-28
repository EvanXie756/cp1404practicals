"""
Program to calculate and display a user's bonus on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales <= 1000:
        total = sales * 0.1
        print(f"Your total: ${total:}")
        sales = float(input("Enter sales: $"))
    else:
        total = sales * 1.5
        print(f"Your total: ${total:}")
