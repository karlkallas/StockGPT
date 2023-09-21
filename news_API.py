from newsapi import NewsApiClient
from datetime import datetime, timedelta

def get_news(company_name):
    today = datetime.today().date()
    yesterday = datetime.today().date() - timedelta(days=1)
    newsapi = NewsApiClient(api_key='d75ff0aca92c45eb8e76e297bbbcfd4a')
    all_articles = newsapi.get_everything(q=company_name,
                                        #   sources='bbc-news,the-verge',
                                        #   domains='bbc.co.uk,techcrunch.com',
                                        from_param=yesterday,
                                        to=today,
                                        language='en',
                                        sort_by='popularity',
                                        page=1)

    return all_articles["articles"][:15]