from app import app, db
from app.models import User

# Проверка и создание базы данных, если она отсутствует
def initialize_database():
    with app.app_context():
        db.create_all()
        print("База данных успешно создана или уже существует.")

if __name__ == '__main__':
    # Инициализация базы данных перед запуском приложения
    initialize_database()
    # Запуск Flask-приложения
    app.run(debug=True)