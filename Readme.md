# Django Auth App с Docker compose

Простое Django-приложение с авторизацией (логин/логаут) в Docker-compose. Главная страница показывает статус авторизации. и используемое БД

Миграции проводятся автоматически, web ждет работу Postgresql иначе миграции или другие операции не пройдут и приложение крашится. Взят файл db.sqlite3 из задания 1 для теста авторизации, если постгрес не поднимется покажет путь к sqlite

Как запустить проект у себя:
```bash
git clone git@github.com:adresmoke/djangowithcompose.git
cd djangowithcompose
sudo docker compsoe up -d
```
Остановить и удалить контейнер:
```bash
sudo docker compsoe down
```
login: 123
passwd: 123

![После авторизации](img/1.png)
![homepage](img/2.png)