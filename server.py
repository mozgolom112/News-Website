from app import app
from app.api.news import get_top_news, add_news
if __name__ == "__main__":
    #test
    """
    print('Q')
    result = get_top_news()
    print(result)
    add_news(result)
    """
    #test

    app.run(debug=False)