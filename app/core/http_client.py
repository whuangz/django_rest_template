import requests
from . logger import Logger

'''
    HTTP Client module.
    Valid function parameters (kwargs):
        - headers
        - params
        - data
        - json
        - cookies
        - auth
        - files
        - timeout
'''

def send(method, url, **kwargs):
    headers = kwargs.get('headers', {})
    params = kwargs.get('params', {})
    data = kwargs.get('data', {})
    json = kwargs.get('json', {})
    
    response = requests.request(method, url, **kwargs)

    try:
        Logger().info("[HTTP Client] Method: {}, Url: {}\n [HTTP Client] Headers: {}\n [HTTP Client] Params: {}\n [HTTP Client] Data: {}\n [HTTP Client] Json: {}\n [HTTP Client] Response Status: {}\n [HTTP Client] Response Payload: {}".format(method, url, headers, params, data, json, response.status_code, response.json()))
    except Exception as e:
        pass

    return response

def get(url, **kwargs):
    return send("GET", url, **kwargs)

def post(url, **kwargs):
    return send("POST", url, **kwargs)

def put(url, **kwargs):
    return send("PUT", url, **kwargs)

def patch(url, **kwargs):
    return send("PATCH", url, **kwargs)

def delete(url, **kwargs):
    return send("DELETE", url, **kwargs)