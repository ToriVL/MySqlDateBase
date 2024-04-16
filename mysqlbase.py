import mysql.connector

# Настройки подключения
host = '127.0.0.1'
port = 3306
database = 'employees'
user = 'root'
password = 'root'

try:
    # Подключение к базе данных
    connection = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print("Подключение успешно.")

        # Здесь можно выполнять операции с базой данных

        # Пример выполнения SQL-запроса
        cursor = connection.cursor()
        cursor.execute("SELECT YEAR(to_date) AS yeard, round(avg(salary),2) AS average_salary "
                       "FROM salaries "
                       "GROUP BY yeard "
                       "order by yeard")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()

    else:
        print("Ошибка подключения.")

except mysql.connector.Error as error:
    print("Ошибка при работе с MySQL:", error)

finally:
    # Закрытие подключения
    if 'connection' in locals():
        connection.close()
        print("Подключение закрыто.")
