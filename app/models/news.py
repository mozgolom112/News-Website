from app import database as db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class News(db.Model):
    __tablename__ = 'News'

    id = db.Column(db.Integer, primary_key = True) #реализовать UUID вместо seq
    
    #ответ от api
    title = db.Column(db.String(300))
    description = db.Column(db.String(500))
    content = db.Column(db.Text)
    url = db.Column(db.String(500)) #ссылка на статью
    images = db.Column(db.String(500)) #ссылки на картинки разделенные ';'
    published_time = db.Column(db.DateTime()) #"yyyy-MM-ddTHH:mm:SSZ" UTC-формат
    
    source = db.Column(db.String(100)) #название или ссылка на новостной сайт
    author = db.Column(db.String(100))
    
    #теги
    category = db.Column(db.Integer, db.ForeignKey('Categories.id')) #категория
    language = db.Column(db.Integer, db.ForeignKey('Language_codes.id')) #язык статьи
    country = db.Column(db.Integer, db.ForeignKey('Country_codes.id')) #запрос специфика страны

    #социалка
    views = db.Column(db.Integer)
    comments = db.Column(db.Integer)

    #для бизнес-логики
    search_query = db.Column(db.Integer, db.ForeignKey('Search_queries.id')) #запросы пользователей
    keywords = db.Column(db.String(1000)) #ключевые слова(некоторые будут получены при слиянии). Разделитель ';'


    #не создается в диаграмме, но упращает работу. См. документацию SQLAlchemy
    

    def __init__(self, title = None, description = None, content = None, 
                url = None, images = None, published_time = None, 
                source = None, author = None, category = None,
                language = None,  country = None, views = 0, 
                comments = 0, keywords = None):
        self.title = title 
        self.description = description 
        self.content = content 
        self.url = url
        self.images = images
        self.published_time = published_time 
        self.source = source 
        self.author = author
        self.category = category
        self.language = language
        self.country = country
        self.views = views
        self.comments = comments
        self.keywords = keywords

    def __repr__(self):
        return '<NewsId {}: {}. Published {} by {}>'.format(self.id, self.title, self.published_time, self.source) 

class Search_query(db.Model):
    __tablename__ = 'Search_queries'

    id = db.Column(db.Integer, primary_key = True)
    query = db.Column(db.String(100))
    last_time_update = db.Column(db.DateTime())
    counts = db.Column(db.Integer) #количество полученных новостей
    http_query = db.Column(db.String(1000))


    def __init__(self,query = None, last_time_update = None, 
                counts = None, http_query = None):
        self.query = query
        self.last_time_update = last_time_update
        self.counts = counts
        self.http_query = http_query
    
    def __repr__(self):
        return '<ID {}. Query = {}. LTU = {}>'.format(self.id, self.query, self.last_time_update)

class Category(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(150))
    decription = db.Column(db.String(150))
    age_max = db.Column(db.Integer) #для ограничения возраста

    def __init__(self, category = None, decription = None, age_max = None):
        self.category = category
        self.decription = decription
        self.age_max = age_max
    
    def __repr__(self):
        return '<Id {}. Category {}>'.format(self.id, self.category)

class Language_code(db.Model):
    __tablename__ = 'Language_codes'
    id = db.Column(db.Integer, primary_key = True)
    lang_code = db.Column(db.String(10), unique = True)
    language = db.Column(db.String(30))
    decription = db.Column(db.String(150))

    def __init__(self, language = None, lang_code = None, decription = None):
        self.language = language
        self.lang_code = lang_code
        self.decription = decription
    
    def __repr__(self):
        return '<LangId: {}. Lang {}>'.format(self.id, self.language)


class Country_code(db.Model):
    __tablename__ = 'Country_codes'
    id = db.Column(db.Integer, primary_key = True)
    country_code = db.Column(db.String(10), unique = True)
    country = db.Column(db.String(30))
    decription = db.Column(db.String(150))

    def __init__(self, country = None, country_code = None, decription = None):
        self.country = country
        self.country_code = country_code
        self.decription = decription
    
    def __repr__(self):
        return '<CountryId {}. Country {}>'.format(self.id, self.country)