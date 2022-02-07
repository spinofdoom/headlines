# headlines
Top news sites are often beautifully designed, but their links don't often show at quick glance which articles have been read.
This Python script seeks to address that. When you run headlines.py, it:

   - grabs top headlines from NYT, Guardian (U.S.), AJ: English, and WaPo through json API data (no scraping, no guilt), 

   - quickly writes them as standard blue hyperlinks to a plain HTML page, 
      
   - then launches that page in the system default browser.

[Requires Python 3.6 and free API keys from [NewsAPI](https://newsapi.org/register), [NYTimes](https://developer.nytimes.com/get-started) and [The Guardian](https://open-platform.theguardian.com/access/).]
