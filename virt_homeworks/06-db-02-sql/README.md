# Домашнее задание к занятию "6.2. SQL"

## Введение

Перед выполнением задания вы можете ознакомиться с 
[дополнительными материалами](https://github.com/netology-code/virt-homeworks/tree/master/additional/README.md).

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, 
в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.
    
    $ docker run -d --name 6.2sql -e POSTGRES_PASSWORD=p1ostgresql -v/Users/ayajirob/sql/datbase:/var/lib/postgresql/database -v /Users/ayajirob/sql/backup:/var/lib/postgresql/backup postgres:12

    $ docker exec -it 6.2sql /bin/sh
## Задача 2

В БД из задачи 1: 
- создайте пользователя test-admin-user и БД test_db

        $ su - postgres
        $ createuser -P test-admin-user
        
    Вводим пароль.

        $ createdb test_db

- в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)

        test_db=# CREATE TABLE orders (id SERIAL PRIMARY KEY, name TEXT, price INTEGER);
        test_db-# CREATE TABLE clients (id SERIAL PRIMARY KEY, second_name TEXT, country TEXT, purchase INT, FOREIGN KEY (purchase) REFERENCES orders (id));
        test_db-#CREATE INDEX country_index on clients (country);

- предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db

        test_db=# GRANT ALL ON clients TO "test-admin-user";
        test_db=# GRANT ALL ON orders TO "test-admin-user";
    
    ИЛИ

        test_db=# GRANT ALL PRIVILEGES ON DATABASE "test_db" TO "test-admin-user";

- создайте пользователя test-simple-user

        test_db=# CREATE USER test-simple-user;

- предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db

        test_db=# GRANT SELECT, INSERT, UPDATE, DELETE ON orders TO "test-simple-user";
        test_db=# GRANT SELECT, INSERT, UPDATE, DELETE ON clients TO "test-simple-user";

Таблица orders:
- id (serial primary key)
- наименование (string)
- цена (integer)

Таблица clients:
- id (serial primary key)
- фамилия (string)
- страна проживания (string, index)
- заказ (foreign key orders)

Приведите:
- итоговый список БД после выполнения пунктов выше,

![Список БД](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D0%91%D0%94.png)

- описание таблиц (describe)

![Описание orders](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/%D0%9E%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20orders.png)

![Описание clients](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/%D0%9E%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20clients.png)

- SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
    
    Внутри test_db выполнить такую команду:
        
        test_db=# \dp *

- список пользователей с правами над таблицами test_db

![Список пользователей](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9.png)

## Задача 3

Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders

|Наименование|цена|
|------------|----|
|Шоколад| 10 |
|Принтер| 3000 |
|Книга| 500 |
|Монитор| 7000|
|Гитара| 4000|

    INSERT INTO orders VALUES (1, chocolate, 10), (2, 'printer', 3000), (3, 'book', 500), (4, 'monitor', 7000), (5, 'guitar', 4000);

Таблица clients

|ФИО|Страна проживания|
|------------|----|
|Иванов Иван Иванович| USA |
|Петров Петр Петрович| Canada |
|Иоганн Себастьян Бах| Japan |
|Ронни Джеймс Дио| Russia|
|Ritchie Blackmore| Russia|

    INSERT INTO clients VALUES (1, 'Ivanov Ivan Ivanovich', 'USA'), (2, 'Petrov Petr Petrovich', 'Canada'), (3, 'Johann Sebastian Bach', 'Japan'), (4, 'Ronnie James Dio', 'Russia'), (5, 'Ritchie Blackmore', 'Russia');

Используя SQL синтаксис:
- вычислите количество записей для каждой таблицы 
- приведите в ответе:
    - запросы 

            SELECT MAX(id) FROM orders;
            SELECT MAX(id) FROM clients;

        Или

            SELECT COUNT(id) FROM orders;
            SELECT COUNT(id) FROM clients;

    - результаты их выполнения.

![Select max()](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/Select%20max().png)

## Задача 4

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.

Используя foreign keys свяжите записи из таблиц, согласно таблице:

|ФИО|Заказ|
|------------|----|
|Иванов Иван Иванович| Книга |
|Петров Петр Петрович| Монитор |
|Иоганн Себастьян Бах| Гитара |

Приведите SQL-запросы для выполнения данных операций.

        UPDATE clients SET purchase = 3 WHERE second_name = 'Ivanov Ivan Ivanovich';
        UPDATE clients SET purchase = 4 WHERE second_name = 'Petrov Petr Petrovich';
        UPDATE clients SET purchase = 5 WHERE second_name = 'Johann Sebastian Bach';

![Изменения в purchase](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B2%20purchase.png)

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.

        SELECT second_name FROM clients WHERE purchase IS NOT NULL;

![All who ordere smth](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/All%20who%20ordered%20smth.png)

## Задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 
(используя директиву EXPLAIN).

Приведите получившийся результат и объясните что значат полученные значения.

### Ответ:

![Explain](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-02-sql/Explain.png)

Seq Scan обозначает, что импользуется последовательное блок за блоком чтение из таблицы clients.

Cost - понятие, которое оценивает затратность операции (1.05 - затраты на получение всех строк из моего запроса).

Rows - количество возвращаемых строк в результате моего запроса.

Width - средний размер одной строки в байтах.

## Задача 6

Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).

    pg_dump test_db > /var/lib/postgresql/backup/test_db.dump

Остановите контейнер с PostgreSQL (но не удаляйте volumes).

    docker stop 6.2sql

Поднимите новый пустой контейнер с PostgreSQL.

    docker run -d --name newsql -e POSTGRES_PASSWORD=p1ostgresql postgres:12

    docker exec -it newsql /bin/sh

Восстановите БД test_db в новом контейнере.

    docker run -d --name newsql -e POSTGRES_PASSWORD=p1ostgresql -v /Users/ayajirob/sql/backup:/var/lib/postgresql/backup postgres:12

    docker exec -it newsql /bin/sh

    su - postgres

    createdb test_db

    createuser -P test-admin-user

    createuser -P test-simple-user

    psql test_db < /var/lib/postgresql/backup/test_db.dump



---

