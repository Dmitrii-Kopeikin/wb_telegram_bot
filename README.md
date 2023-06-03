<a name="readme-top"></a>

<br />
<div align="center">
    <h3 align="center">Wildberries telegram bot</h3>

  <p align="center">
    Тестовое задание
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">О проекте</a>
      <ul>
        <li><a href="#built-with">Использованные технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Запуск</a>
      <ul>
        <li><a href="#prerequisites">Пререквизиты</a></li>
        <li><a href="#installation">Установка</a></li>
      </ul>
    </li>
    <li><a href="#usage">Использование</a></li>
    <li><a href="#license">Лицензия</a></li>
    <li><a href="#contact">Контакты</a></li>
  </ol>
</details>

## О проекте

### Тестовое задание

<p align="justify">
Телеграмм бот который показывает на каком месте товар находится в поисковой выдаче по определенному поисковому запросу.<br>
Иными словами вы пишите в поисковой строке Платье и артикул (идентификатор товара) - 87989388 находится например на 10 странице на 12 месте.<br>
Бот должен это показать. Показывать место любого заданого артикула по любому заданному поисковому запросу.
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Ипользованные технологии

Бот реализован с помощью библиотеки **telebot**.<br>
Для скраппинга используется **Selenium**, т.к. страница WB является динамической.<br>
**Asyncio**, **Aiohttp** для реализации асинхронного выполения запросов<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Запуск

### Запуск из консоли

1. Из директории проекта:
   ```
   cd 'path_to_project_folder'
   python .\bot.py
   # or
   python3 .\bot.py
   ```

### Пререквизиты

- python = "^3.11"
- telebot = "^0.0.5"
- selenium = "^4.9.1"
- aiohttp = "^3.8.4"

### Установка

1. Установка зависимостей:
   ```
   cd 'path_to_project_folder'
   pip install -r requerements.txt
   ```
2. Переименовать 'config/config_local.py' в 'config/config.py'.
3. Получить TOKEN для бота, с помощью [@BotFather](https://t.me/botfather)
4. Вписать в 'config/config.py' токен телеграм-бота.
   ```
   # Telegram-bot token
   TOKEN = 'Вставить TOKEN сюда'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Использование

Бот имеет только две команды:

1. /start - показать описание и инструкцию.
2. Поиск. При получении тестового сообщения, оно проверяется на валидность: "Поисковый запрос 'Артикул'". Например: "велосипед детский 145296859". Если запрос валиден, то он поступает в обработку.

## Лицензия

MIT License. Подробнее в файле `LICENSE.txt`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Контакты

Копейкин Дмитрий.<br>
email: kopeikindp@gmail.com<br>
LinkedIn: [https://www.linkedin.com/in/dmitrii-kopeikin/](linkedin-url)

Project Link: [https://github.com/Dmitrii-Kopeikin/wb_telegram_bot](https://github.com/Dmitrii-Kopeikin/wb_telegram_bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
