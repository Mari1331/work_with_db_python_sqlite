import sqlite3
# NULL(None), INTEGER (int), REAL(float), TEXT (str), BLOB(bytes), INTEGER PRIMARY KEY AUTOINCREMENT - первичный ключ с автоматическим добавдением
# ограничения NOT NULL - не может быть пустой, PRIMARY KEY - первичный ключ
try:
    conn = sqlite3.connect('sqlite_database.db')
    # соединение или создание БД
    cursor = conn.cursor()
    # создали объект курсорe у объекта соединения
    print('База данных подключена к SQLite')
    cursor.execute('''CREATE TABLE SQL_DEVELOPER
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    joing_date TEXT,
    salary REAL NOT NULL);''')
    # можно было в отдельную перемен сохранить SQL-запоос
    #с помощью метода выполнить объекта курсор выполнили создание таблицы
    print('создана таблица SQL_DEVELOPER')
    cursor.execute('''INSERT INTO SQL_DEVELOPER (name, surname, email, joing_date, salary)
        VALUES ('Kate', 'Ivanova', 'asdf@mail.ru', '25-06-2022', 5035.24),
        ('Petr', 'Smirnov', 'petr@gmail.com', '11-08-2022', 3035.00),
         ('Sergei', 'Shtorm', 'seryi111@gmail.com', '11-08-2022', 3035.00);''')
    # вставили зачения в бд
    print('Внесены значения в таблицу')
    conn.commit()
    #сохранены данные, доступны в след сеансах
    print('Сохранены изменения в БД и таблице')
    
    cursor.close()
    #закрыть соединение
    
except sqlite3.Error as error:
    print('Ошибка при подключении', error)

finally:
    if (conn):
        conn.close()
        print('Соединение с SQLite закрыто')