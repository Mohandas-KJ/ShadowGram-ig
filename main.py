from shadowmodules.Banner import showBanner
from shadowmodules.Downloader import download_from_url

if "__main__" == __name__:
    showBanner()
    url = input('Enter url: ')
    download_from_url(url)