import json
import urllib.request
import urllib.error

def get_pilot(nome):
    url = 'https://swapi.co/api/people/'
    params = {'search':nome}
    url_values = urllib.parse.urlencode(params)
    url_total = url + '?' + url_values
    aux = get_url(url_total)
    if type(aux) == str:
        return False
    else:
        if aux['count'] == 0:
            return False
        else:
            return aux['results'][0]

def get_ship(url):
    aux = get_url(url)
    if type(aux) == str:
        return False
    else:
        return aux

def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers) 
    try:
        con = urllib.request.urlopen( req )
        aux = con.read()
        return json.loads(aux)
    except urllib.error.URLError as e:
        return e.reason