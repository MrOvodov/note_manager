cur_status = "В процессе."
status_lst = [1,2,3]
msg = (f"Текущий статус заметки: {cur_status}\n"
       f"Выберите новый статус заметки."
       f"Доступные статусы:\n"
       f"1. Выполнено\n"
       f"2. В процессе\n"
       f"3. Отложено")
print(msg)
while True:
    new_status_int = input('Ваш выбор: ')
    if not new_status_int.isdigit():
        print("Введите число, пожалуйста.")
    else:
        new_status_int =int(new_status_int)
        if not new_status_int in status_lst:
            print("Некорректный ввод. Попробуйте ещё раз.")
        else:
            if new_status_int == 1:
                new_status_txt = "Выполнено."
            elif new_status_int == 2:
                new_status_txt = "В процессе."
            elif new_status_int == 3:
                new_status_txt = "Отложено."
            if new_status_txt == cur_status:
                print("Статус совпадает.")
            else:
                cur_status=new_status_txt
                print(f"Статус заявки успешно обновлён на {cur_status}.")
                break



















