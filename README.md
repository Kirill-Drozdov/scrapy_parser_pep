## О проекте:

Данный проект представляет собой асинхронный парсер документации PEP,
написанный на фреймворке Scrapy.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Kirill-Drozdov/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
py -3.9 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Для работы с парсером необходимо ввести команду в терминал:

```
scrapy crawl pep
```

Все данные будут сохранены в 2 файла формата .csv
в директорию results/:

```
pep_2023-01-28T06-36-08.csv
status_summary_2023-01-28_11-36-24.csv
```

## Об авторе проекта:
Проект выполнил студент Яндекс Практикума -
Дроздов К.С. (https://github.com/Kirill-Drozdov)