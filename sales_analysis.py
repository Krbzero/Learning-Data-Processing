data = [
    {"product": "Mouse", "price": 50, "quantity": 10},
    {"product": "Keyboard", "price": 120, "quantity": 5},
    {"product": "Monitor", "price": 900, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 7},
    {"product": "Keyboard", "price": 120, "quantity": 3},
]

revenue = {}
units_sold = {}

for item in data:
    name = item["product"]
    value = item["price"] * item["quantity"]

    revenue[name] = revenue.get(name, 0) + value
    units_sold[name] = units_sold.get(name, 0) + item["quantity"]

most_sold_product = max(units_sold, key=units_sold.get)
highest_revenue_product = max(revenue, key=revenue.get)
total_revenue = sum(revenue.values())

print("Revenue per product:", revenue)
print("Units sold:", units_sold)
print("Most sold product:", most_sold_product)
print("Product with highest revenue:", highest_revenue_product)
print("Total revenue:", total_revenue)