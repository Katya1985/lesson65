2024/02/01 00:00|Домашнее задание по теме "План написания админ панели"
Цель: написать простейшие CRUD функции для взаимодействия с базой данных.

Задача "Продуктовая база":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните ранее написанный код для Telegram-бота:
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - текст
price(цена) - целое число (не пустой)
get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.

Изменения в Telegram-бот:
В самом начале запускайте ранее написанную функцию get_all_products.
Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов функцию get_all_products. Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

Пример результата выполнения программы:
Добавленные записи в таблицу Product и их отображение в Telegram-bot:



Примечания:
Название продуктов и картинок к ним можете выбрать самостоятельно. (Минимум 4)
Файлы module_14_4.py, crud_functions.py, а также файл с базой данных и таблицей Products загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
