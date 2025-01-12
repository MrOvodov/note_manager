import datetime
username=input('Введите ваше Имя:')
title=input('Введите заголовок заметки:')
content=input('Введите описание заметки:')
status=input('Введите статус заметки:')
created_date=datetime.date.today().strftime('%d-%m-%Y')
issue_date=input('Введите дату окончания (срок завершения в формате "день-месяц-год", например "10-11-2024", если требуется):')
print(f"{username}, ваша заметка создана {created_date}.", end='\n' + f"Не забудьте завершить её {issue_date}.")