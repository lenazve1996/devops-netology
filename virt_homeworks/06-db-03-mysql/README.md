# Домашнее задание к занятию "6.3. MySQL"

## Введение

Перед выполнением задания вы можете ознакомиться с 
[дополнительными материалами](https://github.com/netology-code/virt-homeworks/tree/master/additional/README.md).

## Задача 1

Используя docker поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.

Ссылка на docker-compose файл: 

    $> docker-compose build
    $> docker-compose up
    $> docker start ayajirob_mysql_1

Изучите [бэкап БД](https://github.com/netology-code/virt-homeworks/tree/master/06-db-03-mysql/test_data) и 
восстановитесь из него.

Перейдите в управляющую консоль `mysql` внутри контейнера.

    $> docker exec -it ayajirob_mysql_1 mysql -u root -p

Используя команду `\h` получите список управляющих команд.

Найдите команду для выдачи статуса БД и **приведите в ответе** из ее вывода версию сервера БД.

    >$ status
    Server version:		8.0.29 MySQL Community Server - GPL

Подключитесь к восстановленной БД и получите список таблиц из этой БД.

    >$ CREATE DATABASE test_database;
    >$  \! mysql test_database < ./docker-entrypoint-initdb.d/test_dump.sql -p
    >$ use test_database
    >$ SHOW TABLES;


**Приведите в ответе** количество записей с `price` > 300.

    >$ SELECT COUNT(price) FROM orders WHERE price > 300;
    +--------------+
    | COUNT(price) |
    +--------------+
    |            1 |
    +--------------+
    1 row in set (0.00 sec)

В следующих заданиях мы будем продолжать работу с данным контейнером.

## Задача 2

Создайте пользователя test в БД c паролем test-pass, используя:
- плагин авторизации mysql_native_password
- срок истечения пароля - 180 дней 
- количество попыток авторизации - 3 
- максимальное количество запросов в час - 100
- аттрибуты пользователя:
    - Фамилия "Pretty"
    - Имя "James"
-


    >$ CREATE USER 'test'@'%' IDENTIFIED WITH mysql_native_password BY 'test-pass' WITH MAX_QUERIES_PER_HOUR 100 PASSWORD EXPIRE INTERVAL 180 DAY FAILED_LOGIN_ATTEMPTS 3 ATTRIBUTE '{"Second_name":"Pretty", "First_name":"James"}';

Предоставьте привелегии пользователю `test` на операции SELECT базы `test_db`.

    >$ GRANT SELECT ON test_database.* TO test;
    
Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю `test` и 
**приведите в ответе к задаче**.
    
    ![user_attributes]()

## Задача 3

Установите профилирование `SET profiling z= 1`.
Изучите вывод профилирования команд `SHOW PROFILES;`.

Исследуйте, какой `engine` используется в таблице БД `test_db` и **приведите в ответе**.

Измените `engine` и **приведите время выполнения и запрос на изменения из профайлера в ответе**:
- на `MyISAM`
- на `InnoDB`

## Задача 4 

Изучите файл `my.cnf` в директории /etc/mysql.

Измените его согласно ТЗ (движок InnoDB):
- Скорость IO важнее сохранности данных
- Нужна компрессия таблиц для экономии места на диске
- Размер буффера с незакомиченными транзакциями 1 Мб
- Буффер кеширования 30% от ОЗУ
- Размер файла логов операций 100 Мб

Приведите в ответе измененный файл `my.cnf`.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
