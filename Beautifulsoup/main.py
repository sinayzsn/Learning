import requests
from bs4 import BeautifulSoup


def search_discogs(artist, song_name, url):
    params = {
        'q': f'{artist} {song_name}',
        'type': 'release',
        'format_exact': 'Vinyl',  # You can modify the format as needed
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Assuming the search results are listed under 'search_results' class
        search_results = soup.find_all(class_='search_results')

        if search_results:
            for result in search_results:
                # Assuming the artist and song name are listed under 'search_result_artist' and 'search_result_title' classes respectively
                result_artist = result.find(class_='search_result_artist').text.strip()
                result_song = result.find(class_='search_result_title').text.strip()

                if artist.lower() in result_artist.lower() and song_name.lower() in result_song.lower():
                    # Assuming the link to the release is under 'a' tag with 'href' attribute
                    release_link = result.find('a', href=True)['href']
                    print(f"Found a match!\nArtist: {result_artist}\nSong: {result_song}\nRelease URL: {release_link}")
                    return release_link

    print("No matching results found.")
    return None


if __name__ == "__main__":
    artist_name = "Seether"
    song_name = "Driven Under"
    discogs_url = "https://www.discogs.com/"

    search_discogs(artist_name, song_name, discogs_url)
