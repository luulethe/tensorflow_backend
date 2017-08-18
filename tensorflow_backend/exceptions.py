import traceback

import logging
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import exceptions

UNKNOWN_ERROR = -1

logger = logging.getLogger('main')


def custom_handler(exc, context=None):
    msg = traceback.format_exc()
    logger.error(msg)

    response = exception_handler(exc, context)
    if response is not None:
        try:
            response.data['error_code'] = exc.error_code
        except:
            response.data['error_code'] = -1

        try:
            response.data['error_message'] = response.data['detail']
            del response.data['detail']
        except:
            pass
        return Response({'error': 'UNKNOWN_ERROR'})

    return response


class BaseAPIException(exceptions.APIException):
    error_code = UNKNOWN_ERROR
    default_detail = 'Unknown error'