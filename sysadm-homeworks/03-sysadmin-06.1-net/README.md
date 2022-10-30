# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

1. Работа c HTTP через телнет.
- Подключитесь утилитой телнет к сайту stackoverflow.com
`telnet stackoverflow.com 80`
- отправьте HTTP запрос
```bash
GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]
```
- В ответе укажите полученный HTTP код, что он означает?

    ## Ответ:
    301 Moved Permanently. Означает что сайт/страница переехала навсегда и запрошенный ресурс был окончательно перемещён на URL, указанный в заголовке `Location`. При таком ответе от сервера браузер перенаправляется страницу, указанную в `Location`.

2. Повторите задание 1 в браузере, используя консоль разработчика F12.
- откройте вкладку `Network`
- отправьте запрос http://stackoverflow.com
- найдите первый ответ HTTP сервера, откройте вкладку `Headers`
- укажите в ответе полученный HTTP код.
- проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?
- приложите скриншот консоли браузера в ответ.

    ## Ответ:
    первый ответ от HTTP сервера имеет Status Code 307 Internal Redirect.
    дольше всего обрабатывался запрос к https://stackoverflow.com/ - 473 ms

![Browser-Network](https://github.com/lenazve1996/devops-netology/blob/master/03-sysadmin-06.1-net/Browser.Network.png)

3. Какой IP адрес у вас в интернете?
    ## Ответ:
     109.252.168.180.
    Сайт для определения ip на домашнем компьютере: https://whoer.net/ru
4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой `whois`

    ## Ответ: 
    PJSC Moscow City Telephone Network NOC

        ~$ whois -h whois.ripe.net 109.252.168.180

5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой `traceroute`

    ## Ответ:
    Пакет проходит сначала через мою сеть.
    Затем через сеть провайдера: 100.102.0.1
    Через автономную систему [AS8359] (видимо, сиситема провайдера)
    И через автономную сиситему googl'a [AS15169]

        ~$ traceroute -an 8.8.8.8

![traceroute](https://github.com/lenazve1996/devops-netology/blob/master/03-sysadmin-06.1-net/traceroute.png)

6. Повторите задание 5 в утилите `mtr`. На каком участке наибольшая задержка - delay?
    ## Ответ:
    Наибольшая задержка на участке под номером 7 с адресом 108.170.250.83 у автономной сиситемы googl'a AS15169. Задержка отражена в поле `StDev`.

        ~$ sudo /usr/local/sbin/mtr -nz 8.8.8.8

![mtr_output](https://github.com/lenazve1996/devops-netology/blob/master/03-sysadmin-06.1-net/mtr_output.png)

7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой `dig`

    ## Ответ:
    1. корневой сервер: c.root-servers.net
    2. авторизованный сервер: ns-tld5.charlestonroadregistry.com
    3. авторизованный сервер: ns1.zdns.google
    4. Далее А записи, которые уже непосредственно хранят имя хоста и соответствующие ему адреса IPv4: 8.8.8.8 и 8.8.4.4

            ~$ dig +trace @8.8.8.8 dns.google

![dig_output](https://github.com/lenazve1996/devops-netology/blob/master/03-sysadmin-06.1-net/dig_output.png)

8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой `dig`

    ## Ответ:
    Привязано доменное имя `dns.google`

        ~>dig -x 8.8.4.4
        ~>dig -x 8.8.8.8
    ![dig-x](https://github.com/lenazve1996/devops-netology/blob/master/03-sysadmin-06.1-net/dig-x.png)

