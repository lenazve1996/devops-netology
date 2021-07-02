# Домашнее задание к занятию "3.5. Файловые системы"

1. Узнайте о [sparse](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D1%80%D0%B5%D0%B6%D1%91%D0%BD%D0%BD%D1%8B%D0%B9_%D1%84%D0%B0%D0%B9%D0%BB) (разряженных) файлах.

	> Done.


1. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?

	>Каждому файлу в Linux соответствует индексный дексриптер(номер файла). Именно эти индексные дескрипторы являются истинным именем файла для системы. Они содержат всю информацию о файле. Для человека такая система неудобна, поэтому файлам даются еще и нормальные названия. Они оформляют в виде жесткой ссылки на файл. Права доступа ко всем жестким ссылкам на файл одинаковы, так как определяются одним и тем же индексным дескриптором. Смысл жесткой ссылки состоит в возможности поместить в разные каталоги записи об одном и том же файле, без многократного копирования этого файла во все каталоги, где нужна запись о нем.

1. Сделайте `vagrant destroy` на имеющийся инстанс Ubuntu. Замените содержимое Vagrantfile следующим:

    ```bash
    Vagrant.configure("2") do |config|
      config.vm.box = "bento/ubuntu-20.04"
      config.vm.provider :virtualbox do |vb|
        lvm_experiments_disk0_path = "/tmp/lvm_experiments_disk0.vmdk"
        lvm_experiments_disk1_path = "/tmp/lvm_experiments_disk1.vmdk"
        vb.customize ['createmedium', '--filename', lvm_experiments_disk0_path, '--size', 2560]
        vb.customize ['createmedium', '--filename', lvm_experiments_disk1_path, '--size', 2560]
        vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk0_path]
        vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk1_path]
      end
    end
    ```

    Данная конфигурация создаст новую виртуальную машину с двумя дополнительными неразмеченными дисками по 2.5 Гб.

1. Используя `fdisk`, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.

	> Done. Доп. диски у меня - это /dev/sdb, /dev/sdc.Разбила диск /dev/sdc. Результат:

	![Fdisk](https://github.com/lenazve1996/imagesforreadme/blob/main/Fdisc.png)

	>Инструкция тут: https://andreyex.ru/linux/komanda-fdisk-v-linux-sozdanie-razdelov-diska/
1. Используя `sfdisk`, перенесите данную таблицу разделов на второй диск.

	>Done. Перенесла таблицу разделов диск /dev/sdc на диск /dev/sdb следующими командами:

		sfdisk -d /dev/sdc > partitions-sdc.txt
		sfdisk /dev/sdb < partitions-sdc.txt
	>Результат:

	![Sfdisk](https://github.com/lenazve1996/imagesforreadme/blob/main/Sfdisc.png)

1. Соберите `mdadm` RAID1 на паре разделов 2 Гб.

	>Done.

		lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT(смотрим, какие у нас есть устройства)
		sudo mdadm --create --verbose /dev/md/raid1 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1 (создаем массив)
		cat /proc/mdstat (проверяем активен ли массив)
1. Соберите `mdadm` RAID0 на второй паре маленьких разделов.

	>Done.

		lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT (смотрим, какие у нас есть устройства)
		sudo mdadm --create --verbose /dev/md/raid0 --level=0 --raid-devices=2 /dev/sdb2 /dev/sdc2 (создаем массив)
		cat /proc/mdstat (проверяем, что массив успешно создан)
	Оба массива активны:

	![RAID1, RAID0](https://github.com/lenazve1996/imagesforreadme/blob/main/RAID1%2C%20RAID0.png)

1. Создайте 2 независимых PV на получившихся md-устройствах.
	>Done. RAID0 у меня расположен в /dev/md126, а  RAID1 в
	/dev/md127.

		vagrant@vagrant:~$ sudo pvcreate /dev/md127 /dev/md126

		Physical volume "/dev/md127" successfully created.
		Physical volume "/dev/md126" successfully created.

1. Создайте общую volume-group на этих двух PV.

	>Done.

		vagrant@vagrant:~$ sudo vgcreate vg01 /dev/md127 /dev/md126

  		Volume group "vg01" successfully created

1. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.

	>Done.

		vagrant@vagrant:~$ sudo lvcreate -L 100M -n lvol1 vg01 /dev/md126
		
		Logical volume "lvol1" created.
	> Проверить, что LV установился над верным PV можно командной `sudo lvs -a -o +devices`
	![Lvcreate](https://github.com/lenazve1996/imagesforreadme/blob/main/Lvcreate.png)

1. Создайте `mkfs.ext4` ФС на получившемся LV.

	>Done.
		vagrant@vagrant:~$ sudo mke2fs -t ext4 -L DATA /dev/vg01/lvol1
		mke2fs 1.45.5 (07-Jan-2020)

		Creating filesystem with 25600 4k blocks and 25600 inodes

		Allocating group tables: done
		Writing inode tables: done
		Creating journal (1024 blocks): done
		Writing superblocks and filesystem accounting information: done

1. Смонтируйте этот раздел в любую директорию, например, `/tmp/new`.

	>Done.

		vagrant@vagrant:/$ sudo mount -v -t ext4 /dev/vg01/lvol1 /tmp/new

		mount: /dev/mapper/vg01-lvol1 mounted on /tmp/new.

1. Поместите туда тестовый файл, например `wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz`.

	>Done.

1. Прикрепите вывод `lsblk`.
	
	>Прикрепляю

	![lsblk](https://github.com/lenazve1996/imagesforreadme/blob/main/lsblk.png)

1. Протестируйте целостность файла:

    ```bash
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```
	>Все ок.
1. Используя pvmove, переместите содержимое PV с RAID0 на RAID1.
	>Done.

		vagrant@vagrant:/$ sudo pvmove /dev/md126 /dev/md127
		
		/dev/md126: Moved: 24.00%
		/dev/md126: Moved: 100.00%

1. Сделайте `--fail` на устройство в вашем RAID1 md.

1. Подтвердите выводом `dmesg`, что RAID1 работает в деградированном состоянии.

1. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:

    ```bash
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```

1. Погасите тестовый хост, `vagrant destroy`.

 
 ---

### Как оформить ДЗ?

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в [Google Docs](https://docs.google.com/document/u/0/?tgif=d) и отправить в личном кабинете на проверку ссылку на ваш документ.
Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.1. Введение в DevOps — Сусанна Алиева"
Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка). 
Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Любые вопросы по решению задач задавайте в чате Slack.

---
