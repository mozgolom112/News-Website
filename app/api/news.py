from settings import NEWSAPI_API_KEY as API_KEY
#https://newsapi.org/docs/client-libraries/python
import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=' + API_KEY)

respounse = requests.get(url)
if __name__ == "__main__":
    print( respounse.json())


