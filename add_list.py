import datetime
#--------------------------------
titles=[]
username=input('Введите ваше Имя:')
content=input('Введите описание заметки:')
created_date=datetime.date.today().strftime('%d-%m-%Y')
issue_date=input('Введите дату окончания (срок завершения в формате "день-месяц-год", например "10-11-2024", если требуется):')
status=input('Введите статус заметки:')
title1 = input('Введите заголовок один: ')
title2 = input('Введите заголовок два: ')
title3 = input('Введите заголовок три: ')
#--------------------------------
titles.append(title1)
titles.append(title2)
titles.append(title3)
#titles = [title1,title2,title3]
#--------------------------------
print(f"{username}\n"
      f"{content}\n"
      f"{created_date[:5]}\n"
      f"{issue_date[:5]}\n"
      f"{status}\n"
      f"{titles[:3]}")

