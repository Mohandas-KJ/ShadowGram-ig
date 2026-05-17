#imports
import instaloader
import os

def download_from_url(url):

    os.makedirs("downloads",exist_ok=True)

    L = instaloader.Instaloader()

    #shortcode extraction
    shortcode = url.split("/")[-2]

    post = instaloader.Post.from_shortcode(
        L.context,
        shortcode
    )

    L.download_post(post,target="downloads")

    print("Download Complete")