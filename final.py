import datetime
#---------------------------------
username=input('Введите ваше Имя:')
content=input('Введите описание заметки:')
status=input('Введите статус заметки:')
created_date=datetime.date.today().strftime("%d-%m-%y")
refresh_date=input('Введите дату изменения (В формате "день-месяц-год", например "10-11-2024", если требуется):')
title=input('Введите заголовок заметки:')
title1=input('Введите второй заголовок заметки:')
#---------------------------------
note_list = [
    username,
    content,
    status,
    created_date,
    refresh_date,
    [title,title1]
]
#---------------------------------
print(f"{note_list[0]}, ваша заметка создана {note_list[3]}.\n" 
      f"Краткое инфо по ней:\n"
      f" Имя пользователя: {note_list[0]}\n"
      f" Содержание: {note_list[1]}\n"
      f" Статус: {note_list[2]}\n"
      f" Дата создания: {note_list[3][:5]}\n"
      f" Дата изменения:{refresh_date[:5]}\n"
      f" Заголовки: {note_list[5]}"
      )
