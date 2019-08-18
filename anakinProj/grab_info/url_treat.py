import json
import urllib.error
import urllib.request


def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers) 
    try:
        con = urllib.request.urlopen( req )
        aux = con.read()
        return json.loads(aux)
    except urllib.error.URLError as e:
        return e.reason