import httplib2
import json
import urllib

hObj = httplib2.Http('.cache')
wSrc = 'http://www.wikidata.org/w/api.php'
lang = 'en'

def _get(param):
    param['format'] = 'json'
    param = urllib.urlencode(param)
    resp, cont = hObj.request(wSrc + '?' + param)
    return json.dumps(cont)

def search(type, search): #Annoying keywords
    return _get({
        'action': 'wbsearchentities',
        'language': lang,
        'search': search,
        'type': type
    })

def getEntities(ids, props):
    return _get({
        'action': 'wbgetentities',
        'language': lang,
        'ids': ids,
        'props': props
    })

def getClaim(entityId, propertyId):
    return _get({
        'action': 'wbgetclaims',
        'entity': entityId,
        'property': propertyId
    })

def formatDatavalue(datavalue):
    return _get({
        'action': 'wbformatvalue',
        'language': 'text/plain',
        'datavalue': json.loads(datavalue),
        'options': json.dumps({
            'lang': lang,
            'geoformat': 'dms'
        })
    })
