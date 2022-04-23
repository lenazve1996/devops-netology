# Домашнее задание к занятию "6.4. PostgreSQL"

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.

    ddocker run -d --name 6.4sql -e POSTGRES_PASSWORD=p1ostgresql -v/Users/ayajirob/sql/test_data:/var/lib/postgresql/dump -v /Users/ayajirob/sql/6.4backup:/var/lib/postgresql/backup postgres:13
    
Подключитесь к БД PostgreSQL используя `psql`.

Воспользуйтесь командой `\?` для вывода подсказки по имеющимся в `psql` управляющим командам.

**Найдите и приведите** управляющие команды для:
- вывода списка БД
    
        \l

- подключения к БД

        psql -d database_name
        \c database_name

- вывода списка таблиц

        \d

- вывода описания содержимого таблиц

        \d  table_name

- выхода из psql

        \q

## Задача 2

Используя `psql` создайте БД `test_database`.

    CREATE DATABASE test_database

Изучите [бэкап БД](https://github.com/netology-code/virt-homeworks/tree/master/06-db-04-postgresql/test_data).

Восстановите бэкап БД в `test_database`.

    psql test_database < /var/lib/postgresql/dump/test_dump.sql 

Перейдите в управляющую консоль `psql` внутри контейнера.

    psql -d test_database

Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.

        ANALYZE;

Используя таблицу [pg_stats](https://postgrespro.ru/docs/postgresql/12/view-pg-stats), найдите столбец таблицы `orders` 
с наибольшим средним значением размера элементов в байтах.

**Приведите в ответе** команду, которую вы использовали для вычисления и полученный результат.

    SELECT attname, avg_width FROM pg_stats WHERE tablename = 'orders';

Столбец с наибольшим средним значением размера элементов в байтах - это title;

![avg_width](https://github.com/lenazve1996/devops-netology/blob/master/virt_homeworks/06-db-04-postgresql/avg_width.png)

## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и
поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили
провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

    CREATE TABLE orders_1 (CHECK (price > 499)) INHERITS (orders);

    CREATE TABLE orders_2 (CHECK (price <= 499)) INHERITS (orders);

    INSERT INTO orders_1 SELECT * FROM orders WHERE price > 499;

    INSERT INTO orders_2 SELECT * FROM orders WHERE price <= 499;


Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

Можно было создать сразу таблицу c партициями:

    CREATE TABLE orders (id INT, title character varying(80), price INT) PARTITION BY RANGE (price);

    CREATE TABLE orrrders_1 PARTITION OF orrrders FOR VALUES FROM (0) TO (499);

    CREATE TABLE orrrders_2 PARTITION OF orrrders FOR VALUES FROM (499) TO (10000000);

## Задача 4

Используя утилиту `pg_dump` создайте бекап БД `test_database`.

    pg_dump test_database > /var/lib/postgresql/backup/test_database.dump

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца `title` для таблиц `test_database`?

### Ответ:
В тесте бекапа нашла строчки, где создается таблица 'orders'. В них в поле создания title добавила тип даннх 'UNIQUE' к уже существующему типу 'character'.

![]()
![]()
