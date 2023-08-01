import requests
from bs4 import BeautifulSoup


# def search_artist(artist):
artist = "seether"
print("before")
req = requests.get(f"https://everynoise.com/lookup.cgi?who={artist}+&mode=map")
print("after")

status = req.status_code

print(status)

text = req.text

# html_code = '''
# <a href="engenremap-postgrunge.html" target=_parent>post-grunge</a>,
# <a href="engenremap-alternativemetal.html" target=_parent>alternative metal</a>,
# <a href="engenremap-numetal.html" target=_parent>nu metal</a>,
# <a href="engenremap-southafricanrock.html" target=_parent>south african rock</a>
# &nbsp;
# <a href="everynoise1d.cgi?scope=all&root=post-grunge&root=alternative%20metal&root=nu%20metal&root=south%20african%20rock" target=_parent title="go to the list view for these genres">â#
# '''

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(text, 'html.parser')

# Find all anchor tags (<a>) and extract the text (genre names)
genre_names = [a_tag.text for a_tag in soup.find_all('a')]

# Remove any extra whitespace and empty elements from the list
genre_names = [name.strip() for name in genre_names if name.strip()]

print(genre_names[:-2])
