
def total_salary(path: str) -> tuple[int, float]:
  
  with open(path, encoding="utf-8") as file:
    salaries = []
    for line in file:
        try:
          _, salary = line.split(",")
          salaries.append(int(salary))
        except ValueError:
          print(f"Помилка в рядку: {line.strip()}")
    
    if not salaries:
      return 0, 0

    total = sum(salaries)
    average = total / len(salaries)
    return total, average


total, average = total_salary("01/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
