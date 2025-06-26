# Restaurant income prediction
Задание:https://docs.google.com/document/d/1_2Ctpr4bc9CaKcifsbiUU8MVIrn24eBI/edit?usp=sharing&ouid=105181101765127236665&rtpof=true&sd=true

Google Colab:https://colab.research.google.com/drive/109gE4nzS3Nq16h8GLRJSm3g9Bn5nTvTQ?usp=sharing

## Требования

Перед запуском проекта убедитесь, что у вас установлено:
- Python 3.8 или новее
- pip (менеджер пакетов Python)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/PAliaksandrP/practice-restaurant_income.git
cd practice-restaurant_income
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для macOS/Linux:
source venv/bin/activate
```

3. Установка библиотек:
```bash
pip install -r requirements.txt
```

4. Миграция базы данных:
```bash
python manage.py migrate
```

5. Запуск сервера:
```bash
python manage.py runserver
```

Модель уже загружена в json файл и будет загружена при запуске сервера