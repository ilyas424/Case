# Case

Задача:

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

Дополнительное задание:
```
1) Реализовать вэб-страницу, которая будет отображать таблицу со статистикой;
2) Реализовать на исходной вэб-странице возможность авторизации как админ;
3) У админа должна быть своя страница, на которой он может удалять записи из таблицы с информацией о пользователях. При этом удаление должно фиксироваться в таблице статистки
```

Сздание окружение и установка зависимостей:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r ./requirements.txt
```

Установить переменную среды для запуска скрипта:

```
linux, Mac:
export FLASK_APP=hello

Windows:
$env:FLASK_APP="main.py"
```

Создать файл setting.py

```bash
touch setting.py
```

Пример заполнения файла setting.py:

```
DB_HOST = ''
DB_NAME = ''
DB_USER_NAME = ''
DB_PASSWORD = ''
```

Развернуть бд и накатить миграции:

```flask-sqlalchemy
flask db init
flask db migrate
flask db upgrade
```

Запуск приложение :

```run application
flask run
```

Веб-старницы

Форма заполнения:

![image](https://user-images.githubusercontent.com/107006539/234625737-59fc4426-0b5b-4911-ae9d-85f5041b4c0e.png)


Оповощение о успешной отправке:

![image](https://user-images.githubusercontent.com/107006539/234625940-671f33ab-61a2-42b5-9e4c-c5c326dfd8ae.png)


Список Пользователей:

![image](https://user-images.githubusercontent.com/107006539/235811171-c05ab137-1f9e-4d2b-abb4-400c13c05526.png)


Форма авторизации
![image](https://user-images.githubusercontent.com/107006539/235811117-b33e1c70-29aa-4992-ac01-c843a73b2b4f.png)


Таблица со статистикой действий:
![image](https://user-images.githubusercontent.com/107006539/235811222-f3dc3cfd-e675-4ed8-a829-0751821c4675.png)






