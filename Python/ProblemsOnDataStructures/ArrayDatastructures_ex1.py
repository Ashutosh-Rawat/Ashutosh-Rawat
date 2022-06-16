Month = ['January', 'February', 'March', 'April', 'May']
monthly_expenses = [2200, 2350, 2600, 2130, 2190]


def get_price(month_name):
    price_index = Month.index(month_name)
    return monthly_expenses[price_index]


def expense_comparison(month1, month2):
    rate_difference = get_price(month2) - get_price(month1)
    return rate_difference


def find_expense(value):
    for i in monthly_expenses:
        if value==i:
            req_index = monthly_expenses.index(i)
            return Month[req_index]
        else:
            return "No month with that expense"


def add_expense(month, price):
    Month.append(month)
    monthly_expenses.append(price)
    print(f"price of {price} added for {month}")


def change_value(month, new_price):
    req_index = Month.index(month)
    monthly_expenses[req_index] = new_price
    print(f"Price of {new_price} change for month of {month}")


def fix_expense(month, error_price):
    old_price = get_price(month)
    new_price = old_price - error_price
    change_value(month, new_price)


print(f"1. {expense_comparison('January', 'February')}")

price_of_three_months = get_price("January") + get_price("February") + get_price("March")
print(f"2. {price_of_three_months}")

print(f"3. {find_expense(2000)}")

print("4. ", end="")
add_expense("June", 1980)

print("5. ", end="")
fix_expense("April", 200)
