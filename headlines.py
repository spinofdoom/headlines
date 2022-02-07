from datetime import date
from webbrowser import open_new
from os.path import join as pjoin, expanduser
import requests

home = expanduser('~')
now = date.today().day

def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
       return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

ordinal, date_time = ordinal(day), now.strftime("%A, %B the")
pretty_date = f'{date_time} {ordinal}'

news_api_key = ''             #   Save your
guardian_api_key = ''        #   keys here
nyt_api_key = ''

        #  Free API keys can be generated from
        #  News API (https://newsapi.org/register), the
        #  Guardian (https://open-platform.theguardian.com/access/),
        #  and the New York Times (https://developer.nytimes.com/get-started)

if news_api_key == '':
    news_api_key = input('Input NewsAPI key: ')
if guardian_api_key == '':                              # If you don't have your
    guardian_api_key = input('Input Guardian API key: ') # API keys saved above,
if nyt_api_key == '':                                   # they are prompted for
    nyt_api_key == input('Input New York Times API key')

def news_api_grab(news_source):
    url =  (f'''https://newsapi.org/v2/top-headlines?sources='''
            f'''{news_source}&apiKey={news_api_key}''')
    response = requests.get(url)
    data = response.json()                        #   Grabs NewsApi Headlines
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

def nyt_grab():
    url = (f'''https://api.nytimes.com/svc/topstories/v2/home.json?api-key='''
           f'''{nyt_api_key}''')
    response = requests.get(url)
    data = response.json()
    site, name, body = '', '', ''
    num = 0
    items = data.items()
    for k1, v1 in items:
        if k1 == 'results':
            for article in v1:
                z = article.items()
                for k2, v2 in z:
                    if k2 == 'title':
                        name = v2
                    if k2 == 'url':
                        site = v2
                        num += 1
                        body += f'{num}) <a href="{site}">{name}</a><br><br>\n'
                        if num == 10:
                            return body


def guardian_grab():
    url = (f'''https://content.guardianapis.com/us-news?api-key='''
           f'''{guardian_api_key}''')
    response = requests.get(url)
    data = response.json()
    webUrl, webTitle, body = '', '', ''
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
                            webTitle = v3
                        if k3 == 'webUrl':
                            webUrl = v3
                            num += 1
                            body += f'{num}) <a href="{webUrl}">{webTitle}</a><br><br>\n'
                            if num == 10:
                                return body

body1, body2 = nyt_grab(), guardian_grab()
body3 = news_api_grab('al-jazeera-english')
body4 = news_api_grab('the-washington-post')

message = (f"""<!DOCTYPE html>\n<html>\n"""
    f"""<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>"""
    f"""<link rel="shortcut icon" type="image/jpg" href="favicon.ico"/>"""
    f"""\n<center>\n\n<p><b>New York Times Headlines for {pretty_date}:</b></p>"""
    f"""{body1}\n<p><b>The Guardian Headlines for {pretty_date}:</b></p>"""
    f"""{body2}\n<p><b>Al Jazeera: English Headlines for {pretty_date}:</b></p>"""
    f"""{body3}\n<p><b>The Washington Post Headlines for {pretty_date}:</b></p>"""
    f"""{body4}\n</center>\n</html>""")

end_path = pjoin(home, 'Desktop/headlines.html')         # Writes to Desktop by default
f = open(end_path, 'w')
f.write(message)
f.close()
open_new(f'file://{end_path}')
