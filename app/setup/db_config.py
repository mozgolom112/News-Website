import os
from app.setup.db_settings import db_setting

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2://%(user)s:%(password)s@%(hostname)s/%(database_name)s' % db_setting
    #SQLALCHEMY_DATABASE_URI_MANUAL = 'postgresql:///ghost_dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False #отключение функции уведомления об изменении в БД