import sqlite3
try:
    sql_connect = sqlite3.connect('sql_puthon.db')
    cursor = sql_connect.cursor()
    print('База данных успешно создана')
    #создали БД sql_puthon.db и установили соединение. Если она уже есть, то просто установили соединение
    
    sql_select_query = "select sqlite_version();"
    # в этой строке мы получаем версию БД
    cursor.execute(sql_select_query)
    #это метод у объекта курсор выполняет запрос в БД. Он принимает sql-запрос и возвращает строки из БД. 
    record = cursor.fetchall()
    #получаем результат запроса, fetchall() -все fetchone() - одна строка
    print("Версия базы данных", record)
    cursor.close()
    #  хорошая практика закрытия соединения
    
except sqlite3.Error as error:
    #sqlitr3.Error - класс для обработки любых ошибок и исключений в Пайтон. В error  будет хранится код ошибки
     print('Ошибка при подключении к sqlote', error)
# весь код написан в try-except, что позволяет нам перехватить ислючения и ошибки      
finally:
    if (sql_connect):
        sql_connect.close()
        print('Соединение с SQLite закрыто')
        # хорошая практика закрыть соединение
     