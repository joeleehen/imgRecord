import requests

def getImg(search):
    payload = {'barcode' : str(search), 'token' : 'uEfsYPggGDjMXoVbgYvPEFLYtUnRtucFQibSkSqi'}
    r = requests.get('https://api.discogs.com/database/search', params=payload)
    data = r.json()

    # attempt to extract image URL from json dict
    try:
        results = data[1]
        url = results[0].get('cover_image')
        return url
    except:
        print('an error occurred')
        return 

