titles = []
#-----------------------
while True:
    title = input(f"Введите заголовок заметки\n"
                  f"(Для остановки введите ""Стоп"" или оставьте поле пустым): ")
    if len(title) == 0 or title.lower() == "стоп":
        break
    elif title in titles:
        print(f"Такая заметка уже существует.\n"
              f"Введите другой заголовок.")
        continue
    titles.append(title)
#-----------------------
if len(titles) > 0:
    print(f"Ваш список заголовков:\n")
    for i in titles:
        print(f"{titles.index(i) + 1}. {i}")
else: print(f"Список заголовков пуст.")





