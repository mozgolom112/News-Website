from app.api.settings import NEWSAPI_API_KEY as API_KEY
from app.models.news import News
from app import database as db
import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=' + API_KEY)

respounse = requests.get(url)

def get_top_news(keyword=None, country_code='us'):
       url = 'http://newsapi.org/v2/top-headlines?'
       if keyword is not None:
              try:
                     keyword = str(keyword).lower()
                     url = url + 'q=' + keyword + '&'
              except:
                     pass
       url = url + 'country=' + country_code +'&'
       url = url + 'apiKey=' + API_KEY
       respounse = requests.get(url)
       try:
              respounse = respounse.json()             
       except:
              print('Error. Not possible make json')
              respounse = None
       respounse['full_query'] = url
       return respounse

def add_news(respounse):
       if respounse is None:
              print('Empty json')
              return None
       if respounse.get('status') != 'ok':
              print('Error with api')
              return 'Status - {}. Code - {}. Message: - {}' \
              .format(respounse.get('status'), respounse.get('code'), respounse.get('message'))
       article_count = 0
       for article in respounse.get('articles'):
              article_count = article_count + 1
              news = News(title = article.get('title'), 
                          description = article.get('description'), 
                          url = article.get('url'), 
                          images= article.get('url'), 
                          #published_time =  article.get('url'), 
                          content = article.get('url'), 
                          source = article['source'].get('name'), 
                          author = article.get('author') 
                          )
              db.session.add(news)
       try:
              db.session.commit()
              print('Commit was succesful')
       except:
              db.session.rollback()
              print('Rollback')
       print('Amount article {}'.format(article_count))
       return 0

if __name__ == "__main__":
    res = get_top_news()
    print(res)
   


