# Проект: Асинхронный парсер документов PEP на базе фреймворка Scrapy
[![status](https://github.com/alexpro2022/scrapy_parser_pep/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/scrapy_parser_pep/actions)
[![codecov](https://codecov.io/gh/alexpro2022/scrapy_parser_pep/branch/main/graph/badge.svg?token=Y6507M6P3U)](https://codecov.io/gh/alexpro2022/scrapy_parser_pep)


## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)


## Технологии
<details><summary>Развернуть</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![csv](https://img.shields.io/badge/-csv-464646?logo=python)](https://docs.python.org/3/library/csv.html)
[![collections](https://img.shields.io/badge/-collections-464646?logo=python)](https://docs.python.org/3/library/collections.html)
[![datetime](https://img.shields.io/badge/-datetime-464646?logo=python)](https://docs.python.org/3/library/datetime.html)
[![pathlib](https://img.shields.io/badge/-pathlib-464646?logo=python)](https://docs.python.org/3/library/pathlib.html)
[![typing](https://img.shields.io/badge/-typing-464646?logo=Python)](https://docs.python.org/3/library/typing.html)


**Парсинг - асинхронный фреймворк и селекторы:**

[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?logo=Scrapy)](https://docs.scrapy.org/en/latest/)
[![CSS](https://img.shields.io/badge/-CSS_selectors-464646?logo=CSS)](https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors)
[![XPath](https://img.shields.io/badge/-XPath_selectors-464646?logo=XPath)](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)


**Тестирование:**

[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-cov](https://img.shields.io/badge/-Pytest--cov-464646?logo=Pytest)](https://pytest-cov.readthedocs.io/en/latest/)
[![Coverage](https://img.shields.io/badge/-Coverage-464646?logo=Python)](https://coverage.readthedocs.io/en/latest/)


**CI/CD:**

[![GitHub](https://img.shields.io/badge/-GitHub-464646?logo=GitHub)](https://docs.github.com/en)
[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![Telegram](https://img.shields.io/badge/-Telegram-464646?logo=Telegram)](https://core.telegram.org/api)

[⬆️Оглавление](#оглавление)
</details>


## Описание работы
Парсер собирает ссылки на документы PEP со стартовой страницы по адресу https://peps.python.org/ 
и переходит по каждой ссылке, чтобы получить актуальную информацию о каждом PEP документе.
Парсер работает в асинхронном режиме, что существенно ускоряет выдачу результата парсинга.
Далее парсер обрабатывает информацию и выводит ее в два **.csv**-файла, уникальные названия которых имеют временную метку:
  * В первый файл выводится список [номер, название, статус] всех PEP документов.
  * Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе [статус, количество документов]. В последней строке этого файла выводится итоговая информация [Total, общее количество всех документов].
Файлы создаются в папке **results** в корне проекта.

[⬆️Оглавление](#оглавление)



## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).
1. Клонируйте репозиторий с GitHub:
```bash
git clone https://github.com/alexpro2022/scrapy_parser_pep.git && cd scrapy_parser_pep
```

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Запустите приложение:
```bash
scrapy crawl pep
```

5. Посмотреть содержимое папки **results** можно выполнив команду:
```bash
cd results && ls
```
В командной строке будут выведены имена всех файлов из папки.

6. Содержимое файлов можно посмотреть, выполнив команду:
```bash
cat <имя файла>
```

[⬆️Оглавление](#оглавление)


## Удаление:
Для удаления проекта выполните команду (дважды - если вы в папке results):
```bash
cd .. && rm -fr scrapy_parser_pep && deactivate
```

[⬆️Оглавление](#оглавление)



## Автор
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект-Асинхронный-парсер-документов-PEP-на-базе-фреймворка-Scrapy)
