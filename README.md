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

FastAPI
