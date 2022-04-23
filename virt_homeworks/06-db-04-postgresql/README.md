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

## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и
поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили
провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

## Задача 4

Используя утилиту `pg_dump` создайте бекап БД `test_database`.

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца `title` для таблиц `test_database`?

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
