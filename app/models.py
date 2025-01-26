from app import db, login_manager
from flask_login import UserMixin

# Модель пользователя
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор
    username = db.Column(db.String(100), unique=True, nullable=False)  # Имя пользователя
    password = db.Column(db.String(200), nullable=False)  # Хэшированный пароль
    clicks = db.Column(db.Integer, default=0)  # Счётчик кликов

    def __repr__(self):
        return f"User('{self.username}', Clicks: {self.clicks})"

# Загрузчик пользователя для Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))