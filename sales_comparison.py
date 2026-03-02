days = {
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 90,
    "Thursday": 200,
    "Friday": 180
}

best_day = max(days, key=days.get)
worst_day = min(days, key=days.get)
average_sales = sum(days.values()) / len(days)
days_above_average = [day for day, sales in days.items() if sales > average_sales]

print(f"Best day: {best_day} with {days[best_day]} sales"
      f"\nWorst day: {worst_day} with {days[worst_day]} sales"
      f"\nAverage sales: {average_sales:.2f}"
      f"\nDays above average: {', '.join(days_above_average)}")