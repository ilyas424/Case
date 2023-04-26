# Case


```TASK
Необходимо написать вэб-страницу при помощи стека JS+HTML+CSS.Данная страница собирает личные данные пользователя, после чего
отправляет их на БД. Страница должна состоять из инпутов для вводафамилии, имени и отчества, даты рождения и места работы. Необходимо
организовать проверку вводимых данных либо на стороне страницы,либо на стороне сервера. На странице также присутствует кнопка,
которая позволяет отправить эту информацию в БД. Сама страница должна быть развернута на локальной машине при помощи
фреймворка Flask, который будет связывать вашу страницу и БД.БД может быть организована по реляционному SQL-принципу, при помощи
любого доступного способа (PostgreSQL, SQLite и т.д.). Внутри БД должнобыть 2 таблицы: одна из них отвечает за сбор данных
, другая таблица отображает время, в которое были добавлены данные. Основная программа должна быть написана на Python кроме
сегмента с БД и вэб-страницой.
```


```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r ./requirements.txt
```

```linux, Mac
export FLASK_APP=hello
```

```Windows
$env:FLASK_APP="main.py"
```

```setting.py
create file setting.py
```

```example settings.py file
DB_HOST = ''
DB_NAME = ''
DB_USER_NAME = ''
DB_PASSWORD = ''
```


```flask-sqlalchemy
flask db init
flask db migrate
flask db migrate
```

```run application
flask run
```

```Example
![image](https://user-images.githubusercontent.com/107006539/234623953-1188cf0b-6fd2-4687-b451-d44a8aa747f7.png)
![image](https://user-images.githubusercontent.com/107006539/234624067-73f06f42-83c4-4e95-8d68-585df081ac9f.png)



