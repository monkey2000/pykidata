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
    return json.loads(cont)

def search(type, search):
    return _get({
        'action': 'wbsearchentities',
        'language': lang,
        'search': search,
        'type': type
    })

def query(serach):
    return _get({
        'action': 'query',
        'titles': '|'.join(search),
        'prop': 'revisions',
        'rvprop': 'content'
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
        'datavalue': json.dumps(datavalue),
        'options': json.dumps({
            'lang': lang,
            'geoformat': 'dms'
        })
    })
