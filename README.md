## Тестовое задание

Для запуска на локальном сервере необходимо:

1. Склонировать репозиторий к себе ```git clone https://github.com/e-mois/test_project.git```
2. Установить зависимости ```pip install -r requirements.txt```
3. Зайти в папку ```cd text_project``` и запустить сервер ```export FLASK_APP=app && FLASK_ENV=development && flask run```
4. Запросы можно отправлять с помощью curl 
   * ```curl -X GET http://127.0.0.1:5000/``` для отображения всех постов
   * ```curl -X GET http://127.0.0.1:5000/post/<int:post_id>``` для отображения поста по id с его комментариями
