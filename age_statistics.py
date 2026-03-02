from collections import Counter

ages = [15, 18, 21, 21, 30, 18, 25, 40, 21, 18]

count = len(ages)
max_value = max(ages)
min_value = min(ages)
counter = Counter(ages)
most_frequent_value = counter.most_common(1)[0][0]
average = sum(ages) / count

print(f"Count: {count}"
      f"\nMaximum value: {max_value}"
      f"\nMinimum value: {min_value}"
      f"\nMost frequent value: {most_frequent_value}"
      f"\nAverage: {average:.2f}")