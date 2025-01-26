from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Инициализация Flask-приложения
app = Flask(__name__)

# Настройка конфигурации
app.config['SECRET_KEY'] = 'your_secret_key'  # Секретный ключ для безопасности
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clicker.db'  # Путь к базе данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключение отслеживания изменений

# Инициализация расширений
db = SQLAlchemy(app)  # База данных
bcrypt = Bcrypt(app)  # Шифрование паролей
login_manager = LoginManager(app)  # Управление аутентификацией
login_manager.login_view = 'login'  # Страница для входа

# Импорт маршрутов и моделей
from app import routes, models