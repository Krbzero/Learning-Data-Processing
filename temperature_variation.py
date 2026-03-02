temperatures = [30, 32, 35, 40, 42, 43, 45]

started_to_drop = None

for i in range(1, len(temperatures)):
    if temperatures[i] < temperatures[i - 1]:
        started_to_drop = i
        break

min_temp = min(temperatures)
max_temp = max(temperatures)
variation = max_temp - min_temp
days_above_35 = sum(1 for temp in temperatures if temp > 35)

if started_to_drop is not None:
    print(f"The temperature started to drop on day {started_to_drop + 1}")
else:
    print("The temperature never dropped.")

print(f"Variation between lowest and highest temperature: {variation}°C"
      f"\nNumber of days above 35°C: {days_above_35}")