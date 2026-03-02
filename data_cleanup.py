import math

data = [50, 100, None, 75, "", 200, -10, 150, 80]

cleaned_data = [x for x in data if isinstance(x, (int, float)) and x >= 0]

print("Cleaned data:", cleaned_data)

total_purchases = sum(cleaned_data) if cleaned_data else math.nan
average_purchase = total_purchases / len(cleaned_data) if cleaned_data else math.nan
largest_purchase = max(cleaned_data) if cleaned_data else math.nan

print(f"Total purchases: {total_purchases}"
      f"\nAverage purchase: {average_purchase}"
      f"\nLargest purchase: {largest_purchase}")