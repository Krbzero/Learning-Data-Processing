grades = [7.5, 9.0, 5.5, 6.0, 8.5, 4.0, 10.0, 3.5]

passed = sum(1 for grade in grades if grade >= 6)
failed = sum(1 for grade in grades if grade < 6)
average = sum(grades) / len(grades)
above_average = [grade for grade in grades if grade > average]

print(f"Students who passed: {passed}"
      f"\nStudents who failed: {failed}"
      f"\nClass average: {average:.2f}"
      f"\nGrades above average: {above_average}")