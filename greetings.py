from datetime import datetime
from datetime import date
username, title, content, status = 'Ovodov AV','Studying at SkillPlace','Variables','Active'
created_date=datetime.strftime(date(2025,1,10),'%d-%m-%Y')
issue_date=datetime.strftime(date(2025,10,1),'%d-%m-%Y')
print('Имя пользователя:',username,end=';\n')
print('Заголовок заметки:', title,end=';\n')
print('Описание заметки:',content,end=';\n')
print('Статус заметки:',status,end=';\n')
print('Дата создания:',created_date,end=';\n')
print('Дата истечения:',issue_date,end='.')