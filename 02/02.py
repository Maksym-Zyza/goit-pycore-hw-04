
def get_cats_info(path: str) -> list:
  cats_list = []
  try:
    with open(path, encoding="utf-8") as file:
      for line in file:
        try:
          id, name, age = map(str.strip, line.split(","))
          cat_dict = { "id": id, "name": name, "age": int(age)}
          cats_list.append(cat_dict)
        except ValueError as e:
          print(f"Помилка в рядку: {line.strip()} ({e})")
  except FileNotFoundError:
    print("Файл не знайдено.")
    return []
  except Exception as e:
    print(f"Помилка: {e}")
    return []
  return cats_list

cats_info = get_cats_info("02/cats_file.txt")
print(cats_info)
