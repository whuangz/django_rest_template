import json

from core import http_client
from core.logger import Logger
from base64 import b64encode
from django.contrib.auth.models import User
from django.contrib import auth

oauth_server = "http://host.docker.internal:8000/o"
CLIENT_ID = "bRTlyqOJTjTjRhMlyzdyn4TA1nD6ngEOJcIP0ljz"
CLIENT_SECRET = "UBviT9QA5p5wdeK59UTW4klVaqogQQSEGlYXnMuMtlQWTbHQIaXd2FuJ6zqtSNElOjNooH05zrO9varGchELw9mebftruw58XUpusSCn31q4I6isoW7WE9fOS2gmW5QB"

basic_auth = 'Basic ' + \
    b64encode(str(CLIENT_ID + ':' + CLIENT_SECRET).encode('ascii')
              ).decode("ascii")

scope = 'any'


class Auth():

    def __init__(self):
        pass


def get_token(param, register):
    
    if register == 1:
        try:
            user = User.objects.create_user(username=param["email"],
                                     email=param["email"],
                                     password=param["password"])
        except:
            return None, {"status_code" : 409, "message" : "User already exist"}
    else:
        user = auth.authenticate(username=param["email"], password=param["password"])

        if user is None:
            return None, {"status_code" : 409, "message" : ("User already exist" if register == 1 else "User doesn't exist")}
    

    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': basic_auth
    }

    body = {
        'grant_type': param['type'],
        'scope' : 'read',
        'register' : register
    }

    if param['type'] == 'password':
        body['username'] = param['email']
        body['password'] = param['password']


    token_response = http_client.send(
        'POST', oauth_server + '/v1/token', headers=header, data=body)
    
    if token_response.status_code >= 400:
        return None, {"status_code" : token_response.status_code, "message" : str(token_response.content)}

    token = token_response.json()
    token["user_id"] = user.id
    return token, None


def refresh_token(refresh_token):
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': basic_auth
    }

    body = {
        'scope': scope,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }

    token_response = http_client.send(
        'POST', oauth_server + '/v1/token', headers=header, data=body)
    if token_response.status_code >= 400:
        return None, {"status_code" : token_response.status_code, "message" : str(token_response.content)}

    token = token_response.json()
    return token, None

def authorize_access(bearer):
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': bearer
    }

    body = {
        'scope': scope
    }

    authorized_response = http_client.send(
        'POST', oauth_server + '/v1/authorize', headers=header, data=body)

    if authorized_response.status_code != 200:
        return None, {"status_code": authorized_response.status_code, 
        "message": str(authorized_response.content.decode('utf-8').replace("\"", ""))}

    oauth_user = authorized_response.json()

    return oauth_user, None
