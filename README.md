# Проект: Асинхронный парсер документов PEP на базе фреймворка Scrapy

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка](#установка)
- [Запуск](#запуск-парсера)
- [Автор](#автор)


## Технологии
[![Python](https://warehouse-camo.ingress.cmh1.psfhosted.org/7c5873f1e0f4375465dfebd35bf18f678c74d717/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f7072657474797461626c652e7376673f6c6f676f3d707974686f6e266c6f676f436f6c6f723d464645383733)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=pytest)](https://docs.pytest.org/en/latest/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?logo=Scrapy)](https://docs.scrapy.org/en/latest/)
[![XPath](https://img.shields.io/badge/-XPath_selectors-464646?logo=XPath)](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)
[![CSS](https://img.shields.io/badge/-CSS_selectors-464646?logo=CSS)](https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors)

[⬆️Оглавление](#оглавление)


## Описание работы
Парсер собирает ссылки на документы PEP со стартовой страницы по адресу https://peps.python.org/ 
и переходит по каждой ссылке, чтобы получить актуальную информацию о каждом PEP документе.
Парсер работает в асинхронном режиме, что существенно ускоряет выдачу результата парсинга.
Далее парсер обрабатывает информацию и выводит ее в два **.csv**-файла, уникальные названия которых имеют временную метку:
  * В первый файл выводится список [номер, название, статус] всех PEP документов.
  * Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе [статус, количество документов]. В последней строке этого файла выводится итоговая информация [Total, общее количество всех документов].

[⬆️Оглавление](#оглавление)


## Установка:
1. Клонировать репозиторий с GitHub:
```
git clone git@github.com:alexpro2022/scrapy_parser_pep
```

2. Перейти в созданную директорию проекта:
```
cd scrapy_parser_pep
```

3. Создать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

4. Установить все необходимые зависимости из файла **requirements.txt**:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
pip list
```

[⬆️Оглавление](#оглавление)


## Запуск:

```
(venv) $ scrapy crawl pep
```


## Автор
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект-Асинхронный-парсер-документов-PEP-на-базе-фреймворка-Scrapy)