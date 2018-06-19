from datetime import date
from webbrowser import open_new
from os.path import join as pjoin, expanduser
import requests

home = expanduser('~')
today = str(date.today())
news_api_key = ''        #   Save your keys here.
guardian_api_key = '' #  Free API keys can be generated from
                    #   News API (https://newsapi.org/register) and the
                    # Guardian (https://open-platform.theguardian.com/access/).
if news_api_key == '':
    news_api_key = input('Input NewsAPI key: ')
if guardian_api_key == '':                             # If you don't have your
    guardian_api_key = input('Input Guardian API key: ')# API keys saved above,
                                                       # they are prompted for.

def news_api_grab(news_source):
    url =  (f'''https://newsapi.org/v2/top-headlines?sources='''
            f'''{news_source}&apiKey={news_api_key}''')
    response = requests.get(url)
    data = response.json()                      #   Grabs NewsApi Headlines
    site, name, body = '', '', ''               #   from specified source
    num = 0                                   # (https://newsapi.org/sources)
    items = data.items()
    for k1, v1 in items:
        if k1 == 'articles':
            for article in v1:
                z = article.items()
                for k2, v2 in z:
                    if k2 == 'title':
                        name = v2
                    if k2 == 'url':
                        site = v2
                        num += 1
                        body += f'{num}) <a href="{site}">{name}</a><br><br>\n'
    return body

def guardian_grab():
    url = (f'''https://content.guardianapis.com/us-news?api-key='''
           f'''{guardian_api_key}''')
    response = requests.get(url)
    data = response.json()
    s, n, body = '', '', ''
    num = 0
    items = data.items()
    for k1, v1 in items:             # Grabs Guardian U.S. headlines
        y = v1.items()
        for k2, v2 in y:
            if k2 == 'results':
                for article in v2:
                    z = article.items()
                    for k3, v3 in z:
                        if k3 == 'webTitle':
                            n = v3
                        if k3 == 'webUrl':
                            s = v3
                            num += 1
                            body += f'{num}) <a href="{s}">{n}</a><br><br>\n'
    return body


body1, body2 = news_api_grab('the-new-york-times'), guardian_grab()
body3 = news_api_grab('al-jazeera-english')
body4 = news_api_grab('the-washington-post')

message = (f"""<!DOCTYPE html>\n<html>\n"""
    f"""<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>"""
    f"""\n<center>\n\n<p><b>'New York Times' Headlines for {today}:</b></p>"""
    f"""{body1}\n<p><b>'The Guardian' Headlines for {today}:</b></p>"""
    f"""{body2}\n<p><b>'Al Jazeera: English' Headlines for {today}:</b></p>"""
    f"""{body3}\n<p><b>'The Washington Post' Headlines for {today}:</b></p>"""
    f"""{body4}\n</center>\n</html>""")

end_path = pjoin(home, 'Desktop/headlines.html')
                              # Writes to Desktop by default
f = open(end_path, 'w')
f.write(message)
f.close()
open_new(f'file://{end_path}')
