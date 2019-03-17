from rest_framework.response import Response
from http import HTTPStatus
import json
from django.http import HttpResponse
import traceback
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError

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

    response_body = json.dumps(payload, indent=4, sort_keys=False)

    response = Response(response_body, content_type = 'application/json')
    #response.headers.add('Cache-Control', 'public, max-age=' + str(ttl))
    response.status_code  = status
    #logging().info("[API] response body : {}".format(payload))
    #return response
    return HttpResponse(json.dumps(payload), content_type='application/json')

