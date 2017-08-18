import logging
import traceback
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response

logger = logging.getLogger('main')


class BaseAPIView(APIView):
    def handle_exception(self, exc):
        msg = traceback.format_exc()
        logger.error(msg)
        return super(BaseAPIView, self).handle_exception(exc)

    def post(self, request, *args, **kwargs):
        logger.info("Request %s" % (request.data))
        serializer = self.SERIALIZER_CLASS(data=request.data)
        if not serializer.is_valid():
            raise exceptions.ValidationError(serializer.errors)

        response = self.process(serializer.data)
        logger.info("Request : %s | Response : %s" % (request.data, response))
        return Response(response)