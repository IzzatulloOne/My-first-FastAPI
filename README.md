1. # 🚗 FastAPI Cars & Brands

Небольшой учебный проект на **FastAPI**, который демонстрирует работу API и отображение данных о брендах и автомобилях через HTML-шаблоны.

## 📦 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/fastapi-cars.git
cd fastapi-cars
```
2. Создай и активируй виртуальное окружение
```python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
3.Установи зависимости
```uvicorn main:app --reload```


Теперь API доступно по адресу: 👉 http://127.0.0.1:8000
Документация FastAPI доступна по адресу: 👉 http://127.0.0.1:8000/docs
UI (страница с брендами и машинами) 👉 http://127.0.0.1:8000/ui


📄 Примеры API
Получить список брендов

GET /brands

Пример ответа:
```
[
  {"brand_name": "Nissan", "brand_model": "GTR", "brand_year": 2017, "brand_color": "Black"},
  {"brand_name": "BMW", "brand_model": "M5", "brand_year": 2025, "brand_color": "White"}
]
```

Получить список машин

GET /cars

Пример ответа:
```
[
  {"brand": "Nissan", "engine_volume": 3.8, "power": 600, "fuel_consumption": 11.0, "transmission": "AT", "drive_type": "AWD"},
  {"brand": "BMW", "engine_volume": 4.4, "power": 625, "fuel_consumption": 12.5, "transmission": "AT", "drive_type": "RWD"}
]
```

➕ Как добавлять данные
1. Через UI

Перейди на 👉 http://127.0.0.1:8000/ui
Там появятся блоки Brands и Cars. При нажатии на GET запросы будут показаны добавленные элементы.


2. Через API (POST)

Можно добавить данные напрямую в API:

Добавить бренд

POST /brands
Пример тела запроса:
```
{
  "brand_name": "Toyota",
  "brand_model": "Supra",
  "brand_year": 2020,
  "brand_color": "Red"
}
```

Добавить машину

POST /cars
Пример тела запроса:
```
{
  "brand": "Toyota",
  "engine_volume": 3.0,
  "power": 382,
  "fuel_consumption": 9.5,
  "transmission": "AT",
  "drive_type": "RWD"
}
```

анные автоматически появятся на UI странице (/ui) и будут доступны в GET-запросах.


⚙️ Структура проекта

```
fastapi-cars/
│── main.py               # Основное приложение FastAPI
│── requirements.txt      # Зависимости проекта
│── templates/            # HTML-шаблоны
│   ├── index.html        # Страница с брендами
│   ├── cars.html         # Страница с машинами
│── static/               # (опционально) стили, картинки, иконки
│── README.md             # Этот файл
```



🎨 UI

Для брендов и машин используется стиль в духе FastAPI Docs:

Белая тема

Аккордеон для GET-запросов

Вывод данных в аккуратных карточках

🛠️ Технологии

FastAPI — backend-фреймворк
Jinja2 — шаблонизатор
Uvicorn — ASGI сервер

👨‍💻 Автор

Проект создан для изучения FastAPI.
Ты тоже можешь форкнуть и улучшить 🚀
