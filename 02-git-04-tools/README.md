Для выполнения заданий в этом разделе давайте склонируем репозиторий с исходным кодом терраформа https://github.com/hashicorp/terraform

1.Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea.
	
	Команда: git show aefea
	
	Хэш: aefead2207ef7e2aa5dc81a34aedf0cad4c32545
	Комментарий: Update CHANGELOG.md

2.Какому тегу соответствует коммит 85024d3?
	
	Команда: git show 85024d3
	
	Тэг: v0.12.23

3.Сколько родителей у коммита b8d720? Напишите их хеши.
	
	Команда: git cat-file -p b8d720
	
	2 родителя
	Хэш 1: 56cd7859e05c36c06b56d013b55a252d0bb7e158
	Хэш 2: 9ea88f22fc6269854151c571162c5bcf958bee2b

4.Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.
	
	Команда: git log v0.12.24 --pretty=oneline
	
	Ответ:
	b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
	3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
	6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
	5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
	06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
	d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
	4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
	dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
	225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release

5.Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...) (вместо троеточего перечислены аргументы).
	
	Команды: 
	git log -S 'func providerSource'
	git show 8c928e83589d90a031f811fae52a81be7153e82f
	git show 5af1e6234ab6da412fb8637393c5a17a1b293663
	
	Функция providerSource была создана в комите 8c928e83589d90a031f811fae52a81be7153e82f, так как этот коммит
	был создан раньше.

6.Найдите все коммиты в которых была изменена функция globalPluginDirs.
	
	Команды:
	git grep globalPluginDirs, чтобы найти, в каком файле была объявлена функция globalPluginDirs. Была объявлена в файле: plugins.go.
	git log -L :globalPluginDirs:plugins.go --oneline, чтобы найти все изменения функции в файле plugins.go.
	
	Все коммиты, в которых была изменена функция globalPluginDir:
	78b122055
	52dbf9483
	41ab0aef7
	66ebff90c
	8364383c3
	
7.Кто автор функции synchronizedWriters?
	
	Команды:
	git log -S 'synchronizedWriters' --oneline - чтобы найти в каких коммитах была добавлена или удалены функция ynchronizedWriters.
	git show 5ac311e2a - чтобы посмотреть автора того коммита, где была создана функция ynchronizedWriters.

	Автор: Martin Atkins <mart@degeneration.co.uk>
