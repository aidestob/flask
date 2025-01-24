# Flask
## Описание
Тестовый проект на основе фреймворка Flask
## Требования

### Для запуска проекта требуются следующие пакеты:
* flask
* flask-sqlalchemy
* flask-wtf
* flask-bootstrap

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/aidestob/flask.git`

`cd flask`

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Запустить проект:

`python3 flask run`