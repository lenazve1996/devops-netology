# Домашнее задание к занятию "6.3. MySQL"

## Введение

Перед выполнением задания вы можете ознакомиться с 
[дополнительными материалами](https://github.com/netology-code/virt-homeworks/tree/master/additional/README.md).

## Задача 1

Используя docker поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.

Ссылка на [docker-compose файл](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-03-mysql/docker-compose.yml)

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
    
![user_attributes](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-03-mysql/user_attributes.png)

## Задача 3

Установите профилирование `SET profiling = 1`.
Изучите вывод профилирования команд `SHOW PROFILES;`.

Исследуйте, какой `engine` используется в таблице БД `test_db` и **приведите в ответе**.

    >$ ELECT TABLE_NAME, ENGINE FROM   information_schema.TABLES WHERE  TABLE_SCHEMA = 'test_database';
    +------------+--------+
    | TABLE_NAME | ENGINE |
    +------------+--------+
    | orders     | InnoDB |
    +------------+--------+
    1 row in set (0.05 sec)

Измените `engine` и **приведите время выполнения и запрос на изменения из профайлера в ответе**:
- на `MyISAM`
- на `InnoDB`
-
    
    >$ ALTER TABLE orders ENGINE = MyISAM;
    Query OK, 5 rows affected (0.22 sec)
    Records: 5  Duplicates: 0  Warnings: 0

    >$ALTER TABLE orders ENGINE = InnoDB;
    Query OK, 5 rows affected (0.10 sec)
    Records: 5  Duplicates: 0  Warnings: 0

## Задача 4 

Изучите файл `my.cnf` в директории /etc/mysql.

> `my.cnf` - файл с параметрами, которые задаются при закрузке mysql сервера и/или клиента. То есть любой параметр, который может быть задан при запуске программы mysql через командную строку, можно указать в файле `my.cnf`. Это будет принятый по умолчанию параметр для mysql.

Измените его согласно ТЗ (движок InnoDB):
- Скорость IO важнее сохранности данных
- Нужна компрессия таблиц для экономии места на диске
- Размер буффера с незакомиченными транзакциями 1 Мб
- Буффер кеширования 30% от ОЗУ
- Размер файла логов операций 100 Мб

Приведите в ответе измененный файл `my.cnf`.

    [mysqld]
    pid-file        		= /var/run/mysqld/mysqld.pid
    socket          		= /var/run/mysqld/mysqld.sock
    datadir         		= /var/lib/mysql
    secure-file-priv		= NULL
    innodb_log_file_size		= 100M
    innodb_buffer_pool_size		= 0.57G
    innodb_log_buffer_size		= 1M
    innodb_flush_log_at_trx_commit 	= 2
    innodb_file_per_table		= ON

    # Custom config should go here
    !includedir /etc/mysql/conf.d/


