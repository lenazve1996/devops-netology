# Домашнее задание к занятию "6.2. SQL"

## Введение

Перед выполнением задания вы можете ознакомиться с 
[дополнительными материалами](https://github.com/netology-code/virt-homeworks/tree/master/additional/README.md).

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, 
в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.
    
    $ docker run -d --name 6.2sql -p 5432:5432 -e POSTGRES_PASSWORD=p1ostgresql -v/Users/ayajirob/sql/datbase:/var/lib/postgresql/database -v /Users/ayajirob/sql/backup:/var/lib/postgresql/backup postgres:12
    docker

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

## Задача 4

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.

Используя foreign keys свяжите записи из таблиц, согласно таблице:

|ФИО|Заказ|
|------------|----|
|Иванов Иван Иванович| Книга |
|Петров Петр Петрович| Монитор |
|Иоганн Себастьян Бах| Гитара |

Приведите SQL-запросы для выполнения данных операций.

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.
 
Подсказк - используйте директиву `UPDATE`.

## Задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 
(используя директиву EXPLAIN).

Приведите получившийся результат и объясните что значат полученные значения.

## Задача 6

Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).

Остановите контейнер с PostgreSQL (но не удаляйте volumes).

Поднимите новый пустой контейнер с PostgreSQL.

Восстановите БД test_db в новом контейнере.

Приведите список операций, который вы применяли для бэкапа данных и восстановления. 

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
