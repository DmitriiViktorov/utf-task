# Меню ресторана (Django + DRF)

Этот проект — сервис для управления меню ресторана. 
Он позволяет получать список категорий блюд и их содержимое через API, а также отображать меню на веб-странице.

## Функциональность

- API для получения категорий блюд с опубликованными позициями.
- Веб-страница с отображением меню (Django ListView).
- Фильтрация: в выборку попадают только опубликованные блюда.
- Используется Django ORM + Django REST Framework.

---

## Установка и запуск

### Клонирование репозитория
```bash
git clone https://github.com/DmitriiViktorov/utf-task.git
```

### Создание и активация виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Применение миграций
```bash
cd food-application/
python manage.py migrate
```

### Инициализация данных (создание тестовых категорий и блюд)
```bash
python manage.py check_and_populate
```

### Запуск сервера
```bash
python manage.py runserver
```

### Создание файла .env

Перед запуском необходимо создать файл `.env` в корневой папке проекта и указать в нем настройки окружения.  

В `.env` файле для работы приложения нужно указать следующие ключи:
```ini
DJANGO_SECRET_KEY=your-secret-key
```

После запуска сервис доступен по адресам:

    API: http://127.0.0.1:8000/api/v1/foods/
    Меню (HTML-шаблон): http://127.0.0.1:8000/foods/


## Контактная информация

В случае возникновения вопросов, комментариев, замечаний по работе приложения вы можете связаться со мной:
- Email: viktorovokrl@gmail.com
- Github: https://github.com/DmitriiViktorov
- Telegram: https://t.me/ViktorovDV










