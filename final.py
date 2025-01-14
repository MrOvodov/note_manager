import datetime
username=input('Введите ваше Имя:')
title=input('Введите заголовок заметки:')
title1=input('Введите второй заголовок заметки:')
content=input('Введите описание заметки:')
status=input('Введите статус заметки:')
created_date=datetime.date.today().strftime('%d-%m-%Y')
refresh_date=input('Введите дату изменения (В формате "день-месяц-год", например "10-11-2024", если требуется):')
note_list = [
    username,
    content,
    status,
    created_date,
    refresh_date,
    [title,title1]
    ]
print(note_list)

print(f"{username}, ваша заметка создана {created_date}.", end='\n' + f"Краткое инфо по ней:  {note_list}.")
