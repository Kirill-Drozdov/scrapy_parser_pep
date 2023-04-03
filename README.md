## Scrapy_parser_pep

### О проекте:

Проект представляет собой асинхронный парсер документации PEP,
написанный на фреймворке Scrapy. В результате работы парсера в директории
`results` формируется 2 отчета в формате `.csv`.

* В файле `pep` хранятся все доступные стандарты `PEP`,
их номер, название и статус.

* В файле `status_summary` выведен подсчет стандартов `PEP`
по статусам.

### Технологии
```
python 3.9
Scrapy
```

### Как запустить проект:

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

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
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

Все данные будут сохранены в 2 файла формата `.csv`
в директорию `results`:

```
pep_2023-01-28T06-36-08.csv
status_summary_2023-01-28_11-36-24.csv
```

### Об авторе проекта:
Проект выполнил студент Яндекс Практикума -
[Дроздов К.С.](https://github.com/Kirill-Drozdov)