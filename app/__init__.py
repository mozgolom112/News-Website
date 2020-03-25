from flask import Flask
from app.setup.db_config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#инициируем сервер
app = Flask(__name__)

#подключаем все маршруты
from app.routes import routes
from app.routes import routes2

app.config.from_object(Config)
database = SQLAlchemy(app)
migarate = Migrate(app, database)

#подключаем модели
from app.models import news

#пока просто создаем все модели. 
#001 - сделать через миграцию https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
database.create_all()

from app.api.news import get_top_news

get_top_news()