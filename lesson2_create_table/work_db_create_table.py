import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_database')
    # соединение или создание БД
    sqlite_create_table_query = '''CREATE TABLE SQL_DEVELOPER
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joing_date datetime,
    salary REAL NOT NULL);'''
    
    cursor = sqlite_connection.cursor()
    print('База данных подключена к SQLite')
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Таблица SQLite создана')
    
    cursor.close()
    
except sqlite3.Error as error:
    print('Ошибка при подключении', error)

finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print('Соединение с SQLite закрыто')