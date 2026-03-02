ages = [12, 17, 25, 34, 45, 52, 61, 15, 19, 28, 37]

groups = {"children": 0, "teenagers": 0, "adults": 0, "elderly": 0}

for age in ages:
    if age <= 12:
        groups["children"] += 1
    elif 13 <= age <= 19:
        groups["teenagers"] += 1
    elif 20 <= age <= 59:
        groups["adults"] += 1
    else:
        groups["elderly"] += 1

largest_group = max(groups, key=groups.get)
smallest_group = min(groups, key=groups.get)
adult_percentage = (groups["adults"] / len(ages)) * 100

print(f"Children: {groups['children']}"
      f"\nTeenagers: {groups['teenagers']}"
      f"\nAdults: {groups['adults']}"
      f"\nElderly: {groups['elderly']}"
      f"\nLargest group: {largest_group}"
      f"\nSmallest group: {smallest_group}"
      f"\nAdult percentage: {adult_percentage:.2f}%")