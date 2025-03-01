# Feed edu demo
Django-приложение для создания и прохождения опросов.

## 📜 Описание  
Этот проект позволяет:  
✅ Создавать опросы с различными типами вопросов   
✅ Отправлять опросы пользователям.  
✅ Сохранять ответы.  

---

## 📊 Структура базы данных  
Вот схема БД (ER-диаграмма):  

![Иллюстрация к проекту](https://github.com/AlisherAsd/feed_edu_demo/raw/main/infoapi/img/db.jpg)


## 🚀 Установка и запуск  

### 1️⃣ Клонирование репозитория  
```
git clone https://github.com/AlisherAsd/feed_edu_demo
cd feed_edu_demo
```

2️⃣ Установка зависимостей
```
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```
3️⃣ Применение миграций
```
python manage.py migrate
```
4️⃣ Создание суперпользователя (если нужно)
```
python manage.py createsuperuser
```
5️⃣ Запуск сервера
```
python manage.py runserver
```
By Alisher