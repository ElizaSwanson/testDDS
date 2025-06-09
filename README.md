# Дипломный проект
### "Веб-сервис для управления движением денежных средств (ДДС)
### автор: Насытко Елизавета Сергеевна

условия тестового: https://drive.google.com/file/d/1vbPk2aiMe52pDFW57zMUDMaW7rqrHypc/view

1. Клонируйте репозиторий:

```
https://github.com/ElizaSwanson/testDDS
```
2. Создайте и заполните данными файл <b>.env</b> по шаблону <b>.env.sample</b>, который находится в корне проекта
3. Установите зависимости из файла
```pip install -r requirements.txt```
4. Создайте и примените миграции

```
python manage.py makemigrations
python manage.py migrate
```

5. Если необходимо, загрузите следующие фикстуры:

```
   python manage.py loaddata flowtype_fixture.json --format json
   python manage.py loaddata status_fixture.json --format json
   python manage.py loaddata category_fixture.json --format json
   python manage.py loaddata subcategory_fixture.json --format json
   python manage.py loaddata moneyflow_fixture.json --format json
```
6. Создайте суперпользователя. Введите команду и следуйте инструкциям:

```
python manage.py createsuperuser
```

7. Перейдите по адресу http://127.0.0.1:8000/   и залогиньтесь от имени созданного суперпользователя
8. Основная страница находится по адресу: http://127.0.0.1:8000/moneyflows/


