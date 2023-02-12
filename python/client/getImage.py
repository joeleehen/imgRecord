import requests

def getImageBar(search):
    payload = {'barcode' : str(search), 'token' : 'uEfsYPggGDjMXoVbgYvPEFLYtUnRtucFQibSkSqi'}
    r = requests.get('https://api.discogs.com/database/search', params=payload)
    data = r.json()


    results = data['results']
    # print(results)
    url = results[0].get('cover_image')
    if url:
        return url
    else:
        return 0

def getImageTxt(album, artist):
    if album == "" or artist == "":
        return
    payload = {'release_title' : str(album), 'artist' : str(artist), 'token' : 'uEfsYPggGDjMXoVbgYvPEFLYtUnRtucFQibSkSqi'}
    r = requests.get('https://api.discogs.com/database/search', params=payload)
    data = r.json()

    results = data['results']
    if results:
        url = results[0].get('cover_image')
        if url:
            return url
        else:
            return 0
    else:
        print("ERROR: no album found!")
