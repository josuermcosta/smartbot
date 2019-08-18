import json
import url_treat
import urllib.request

def get_pilot(nome):
    url = 'https://swapi.co/api/people/'
    params = {'search':nome}
    url_values = urllib.parse.urlencode(params)
    url_total = url + '?' + url_values
    aux = url_treat.get_url(url_total)
    if type(aux) == str:
        return False
    else:
        if aux['count'] == 0:
            return False
        else:
            return aux['results']

def get_ship(url):
    aux = url_treat.get_url(url_total)
    if type(aux) == str:
        return False
    else:
        if aux['count'] == 0:
            return False
        else:
            return aux