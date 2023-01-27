import requests

def getImage(search):
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
