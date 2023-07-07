# Resources

**[Main website](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**

# How to use

------------------------------------------------

## To scrape url's

To use urls you have to use the request method to get the html content of the website that you are trying to scrape.
In order to do that you have to implement the following code, and methods.
```python
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request('https://www.metacritic.com/browse/movies/genre/date?page=0', headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req).read()

soup = BeautifulSoup(html_page, 'html.parser')
links = []
for link in soup.findAll('a', attrs={'href': re.compile("^/movie/")}):
    links.append(link.get('href'))

print(links)
```
This method above would get the links from the HTML page that we have sent a request to. 
To get this method to work we have to know what are we going to get from the web page. 

So in my example I want to search a artist with one of the names of the music he/she produced and get the genres of
that music/album.

There were multiple methods that I have found to test these.

**Method Number 1**
```python
from urllib import urlencode
import requests
params = {'search': '7420 Westlake Ter #1210 20817'}
search_url = 'http://www.trulia.com/submit_search/?'
url = search_url + urlencode(params)
r = requests.get(url)
# now you get your desired response.
```

**Method Number 2**
```python
r = requests.post("http://www.trulia.com/homepage.php", data={'searchbox_form': '7420 blahblah'})
```

_These methods are just samples I have found from this questions asked in StackOverFlow_ 
[Here](https://stackoverflow.com/questions/26814049/use-python-requests-library-to-post-data-to-search-box) 

