# semalt.test.work

## Для запуска проекта необходимо:
Добавить себе проект:
```sh
$ git clone https://github.com/georgsby/semalt.test.work.git
```

Проверить версию python:
```sh
$ python --version
```

Обновить до версии 3.5+
```sh
$ update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```
Установить менеджер пакетов pip
```sh
$ sudo apt install python3-pip -y
```
Установить Django:
```sh
$ pip3 install Django
```
Установить virtualenv:
```sh
$ virtualenv -p python3 venv
```
Установить все зависимости проекта:
```sh
$ pip freeze -r requirements.txt
```

Сделать миграции:
```sh
$ python manage.py migrate
```
Запустить проект:
```sh
$ python manage.py runserver
```

## Для использования gulp необходимо:
Установить node.js:
```sh
$ sudo apt-get install -y nodejs
```

Установить gulp глобально:
```sh
$ sudo npm i gulp -g
```
Установить пакеты для разработки:
```sh
$ sudo npm i --save-dev gulp
$ sudo npm i --save-dev gulp-sass
$ sudo npm i --save-dev browser-sync
$ sudo npm i --save-dev gulp-clean
$ sudo npm i --save-dev gulp-cache
$ sudo npm i --save-dev gulp-autoprefixer
```

Запустить gulp:
```sh
$ sudo gulp watch
```
