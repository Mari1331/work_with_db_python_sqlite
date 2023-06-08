import sqlite3
# NULL(None), INTEGER (int), REAL(float), TEXT (str), BLOB(bytes), INTEGER PRIMARY KEY AUTOINCREMENT - первичный ключ с автоматическим добавдением
# ограничения NOT NULL - не может быть пустой, PRIMARY KEY - первичный ключ
try:
    conn = sqlite3.connect('sqlite_database.db')
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM SQL_DEVELOPER ORDER BY surname LIMIT 2 ')
    # for row in cursor.fetchall():
    #     print(*row, sep=' ')
    #fetchall - выбрать все - выводит список кортежей, можно обойти for
    #благодаря выставленному лимиту в запросе мы выведем две первые строки 
    #благодаря ORDER BY - в алфавитном пордке по заданному столбцу
    # ИЛИ
    #можно в формате итератора, смотри ниже
    for row in cursor.execute('''SELECT * FROM SQL_DEVELOPER 
                                WHERE email not like('%mail.ru') ORDER BY surname;'''):
        print(*row)
        
    # Выбираем одну строку запроса
    # res = cursor.fetchone()
    #print(res)
    #fetchone - выбрать одно- выводит в одну строку кортеж из первой строки
    
    # 
    # res = cursor.fetchall()
    # print(res)
    #fetchall - выводит список кортежей
    
    ## for res in cursor.fetchone():
    ##     print(res) - если мы хотим картеж обойти по значениям
    conn.close()
    print('Соединение завершено')
    
except sqlite3.Error as error:
    print('Ошибка при подключении', error)

finally:
    if (conn):
        conn.close()
        print('Соединение с SQLite закрыто')