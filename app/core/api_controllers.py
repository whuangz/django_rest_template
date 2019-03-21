import json
import traceback

from rest_framework.response import Response
from http import HTTPStatus
from django.http import HttpResponse
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError
from .logger import Logger
from auth import Auth

def exception_handler(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except SQLAlchemyError as ex:
            error = f"Exception message [DB]: {str(ex)} {traceback.format_exc()}"
            Logger().error(error)
            return render_json(status=HTTPStatus.INTERNAL_SERVER_ERROR, message = 'DB Exception')
        except APIException as ex:
            status, error_data = ex.http_status, ex.data
            error = f"Exception message [API]: {str(ex)} {traceback.format_exc()}"
            Logger().error(error)
            return render_json(data=error_data, status=status, message='API Exception')
        except Exception as ex:
            error = f"Exception message: {str(ex)} {traceback.format_exc()}"
            Logger().error(error)
            return render_json(status=HTTPStatus.INTERNAL_SERVER_ERROR)
    return wrapper

def render_json(status=HTTPStatus.OK, data=None, serializer=None, as_array=False, message=None, meta=None, ttl = 0):
    if serializer:
        if data == None:
            status = HTTPStatus.NOT_FOUND
        elif as_array:
            data = [serializer(item).data() for item in data]
        else:
            data = serializer(data).data()

    data_key = 'data'
    if status < 200 or status >= 300:
        data_key = 'errors'

    payload = {
        'status' : status,
        'message' : message or status.phrase,
        data_key : data
    }

    if type(meta) == dict:
        payload['meta'] = meta

    
    response = Response(payload, status= status ,content_type = 'application/json')
    response['Cache-Control'] = 'public, max-age=' + str(ttl)
    Logger().info("[API] response body : {}".format(payload))
    return response

