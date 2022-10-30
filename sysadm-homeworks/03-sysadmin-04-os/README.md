# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

1. На лекции мы познакомились с [node_exporter](https://github.com/prometheus/node_exporter/releases). В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой [unit-файл](https://www.freedesktop.org/software/systemd/man/systemd.service.html) для node_exporter:

    * поместите его в автозагрузку,
    * предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на `systemctl cat cron`),
    * удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.

	> done. Порядок выполнения:

		curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz

		sha256sum node_exporter-1.1.2.linux-amd64.tar.gz
		tar xvf node_exporter-1.1.2.linux-amd64.tar.gz

		sudo cp node_exporter-1.1.2.linux-amd64/node_exporter /usr/local/bin

		sudo chown node_exporter:node_exporter /usr/local/bin/node_exporter

		sudo vim /etc/systemd/system/node_exporter.service

	>Содержание файла /etc/systemd/system/node_exporter.service:

		[Unit]
		Description=Node Exporter
		Wants=network-online.target
		After=network-online.target

		[Service]
		User=node_exporter
		Group=node_exporter
		Type=simple
		ExecStart=/usr/local/bin/node_exporter

		[Install]
		WantedBy=multi-user.target

	>После сохранила файл и выполнила следующие команды:

		sudo systemctl daemon-reload

		sudo systemctl start node_exporter

		sudo systemctl status node_exporter

	![Enabled Node Exporter](https://github.com/lenazve1996/imagesforreadme/blob/main/Enabled%20Node%20Exporter%20.png)


1. Ознакомьтесь с опциями node_exporter и выводом `/metrics` по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.

	>Для мониторинга хоста по CPU, памяти, диску и сети я бы выбрала следующие коллекторы:
	cpu, diskstats, ipvs, netclass, meminfo


1. Установите в свою виртуальную машину [Netdata](https://github.com/netdata/netdata). Воспользуйтесь [готовыми пакетами](https://packagecloud.io/netdata/netdata/install) для установки (`sudo apt install -y netdata`). После успешной установки:
    * в конфигурационном файле `/etc/netdata/netdata.conf` в секции [web] замените значение с localhost на `bind to = 0.0.0.0`,
    * добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте `vagrant reload`:

    ```bash
    config.vm.network "forwarded_port", guest: 19999, host: 19999
    ```

    После успешной перезагрузки в браузере *на своем ПК* (не в виртуальной машине) вы должны суметь зайти на `localhost:19999`. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.

	>done. 
	Основные разделы, по котрым собираются метрики по умолчанию отображены в панели справа:
	 System Overview, CPUs, Memory, Disks,  Networking Stack,  IPv4 Networking,  IPv6 Networking,  Network Interfaces и т.д.
	 В комменариях к метрикам указано, что именно собирает этот колеектор, также иногда указано из каких файлов/папок на хосте он берет эту информацию. Также есть некоторые советы или уточнения, на которые нужно обратить внимание.

	 ![Netdata](https://github.com/lenazve1996/imagesforreadme/blob/main/Netdata.png)

1. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?

	>Можно. По таким строкам:

		[    2.427500] systemd[1]: Detected virtualization oracle.
		[    0.152930] Booting paravirtualized kernel on KVM
		[    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
		[    0.003054] CPU MTRRs all blank - 	virtualized system.
1. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?
	> команда /sbin/sysctl -n fs.nr_open или cat /proc/sys/fs/nr_open покажут максимально возможное число открытых файлов для одного процесса. В моем случае 1048576 файлов(что составляет 1024 * 1024).

	>Также максимальный лимит (Hard limit) открытых файлов на процесс для текущего пользователя можно увидеть через команду `ulimit -Hn`. Текущий лимит (Soft limit) открытых файлов на процесс для текущего пользователя можно увидеть через команду `ulimit -Sn`.
1. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.

		unshare -f --pid --mount-proc sleep 3h &
 	>Используем команду `unshare`, которая запускает программы в новых пространствах имен. Создаем новое пространство имен  PID через опцию `--pid`. Монтируем файловую систему proc в точке монтирования через опцию `--mount-proc` (она будет содежать информацию согласно новому пространству имен PID).Опция `-f` запускает указанную программу (в моем случае - sleep 3h) в новом пространстве имен как дочерний процесс (так как это первый процесс в пространстве имен, ему присваевается номер PID - 1).
	
	Через команду `nsenter` проверяем все ли выполнилось корректно:
	
		nsenter --target 2101 --pid --mount ps aux
	![Unshare, nsenter](https://github.com/lenazve1996/imagesforreadme/blob/main/Unshare%2C%20nsenter.png)

1. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?

	>`:(){ :|:& };:` - Вилочная бомба,fork bomb.  Функция, которая параллельно пускает два своих экземпляра. Каждая следующая запускает ещё по два и т.д.

	>Вызов `dmesg` показал такую строчку:

		fork rejected by pids controller in /user.slice/user-1000.slice/session-6.scope

	>Механизм Process Number Controller помог автоматической стабилизации. Контроллер номеров процесса используется для того, чтобы иерархия cgroup могла запретить выполнение любых новых задач fork()’d или clone()’d после достижения определенного предела. В папке `/sys/fs/cgroup/pids/user.slice/user-1000.slice/session-6.scope` содержится файл `pids.max`. В нем установлено значение `max`. Это значит что для моего пользователя/моей сессии количество созданных процессов было не ограничено. Смотрим папку выше. В папке `/sys/fs/cgroup/pids/user.slice/user-1000.slice` файл `pids.max` ограничивает максимальное количество прочессов - 2364. Значит на мою сессию распространялись эти ограничения. Тогда Process Number Controller дал возможность данной fork bomb создать только 2364 новых прочессов.

	>Изменение числа процессов:

	>1. Можно либо измменить кол-во максимально возможных процессов в папке cgroup,согласно этой инструкции (эти настройки будут распространятся на все сессии): https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/pids.html

	>2. Также можно изменить максимально возможное число процессов именно для моей сессии, внеся изменения в файл `/sys/fs/cgroup/pids/user.slice/user-1000.slice/session-6.scope/pids.max`.

	>3. Либо можно изменить кол-во возможных процессов в настройках ядра `/proc/sys/kernel/pid_max`. PID больше значения, которое создержится в этом файле, не выделяются. Таким образом, значение в этом файле также действует как системное ограничение на общее количество процессов и потоков.
