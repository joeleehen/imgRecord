import requests

def getImageBar(search):
    print(search)
    try:
        payload = {'barcode' : str(search), 'token' : 'uEfsYPggGDjMXoVbgYvPEFLYtUnRtucFQibSkSqi'}
        r = requests.get('https://api.discogs.com/database/search', params=payload)
        data = r.json()


        results = data['results']
        # print(results)
        url = results[0].get('cover_image')
        if url:
            return url
        else:
            return
    except:
            return 'https://i.discogs.com/a6wAohfJ1KTLXijU79CjHu7nRUYqVC8mES2O4VnlbIA/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM5MTQ5/MTQtMTM5MjQzNTE1/Ny0yODEwLmpwZWc.jpeg'

def getImageTxt(album, artist):
    if album == "" or artist == "":
        return
    print(album, artist)
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
