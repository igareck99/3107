from requests import get
from requests.auth import HTTPBasicAuth
from secretKeys import weatherAPIkey
import os

baseUrl = 'http://api.weatherapi.com/v1'

def requestByLocations(latitude, longtitude):
    auth = HTTPBasicAuth('apikey', weatherAPIkey)
    params = {'q': '{},{}'.format(latitude, longtitude)}
    r = get(url=baseUrl + '/current.json', params=params,auth=auth)
    return r.json()