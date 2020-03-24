API_KEY = "79f2703915ea40e5982561af7a2147b9"
#https://newsapi.org/docs/client-libraries/python
import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=79f2703915ea40e5982561af7a2147b9')

respounse = requests.get(url)
if __name__ == "__main__":
    print( respounse.json())


