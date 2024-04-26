import pyshorteners
url=input("Enter the URL")
def shortenurl(url):
    k=pyshorteners.Shortener()
    x=k.tinyurl.short(url)
    print(x)
shortenurl(url)