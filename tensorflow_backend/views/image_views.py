import os
from rest_framework import exceptions
from rest_framework.response import Response
import time
from tensorflow_backend import serializers, constant
from tensorflow_backend.exceptions import BaseAPIException
from tensorflow_backend.views.base_views import BaseAPIView
import random
import datetime
from tensorflow_backend import models


class ImageNotificationView(BaseAPIView):
    SERIALIZER_CLASS = serializers.NotificationSerializer

    def process(self, data):
        person, _ = models.Person.objects.get_or_create(name=data["name"])
        image = models.Image.objects.get(name=data["image_id"])
        image.person = person
        image.prob = data["prob"]
        image.status = models.Image.SUCCESS
        image.save()

        return {"status": "ok"}


class UploadView(BaseAPIView):
    SERIALIZER_CLASS = serializers.ImageUploadSerializer

    def post(self, request, *args, **kwargs):
        if not os.path.exists(constant.DIR_IMAGE_STORAGE):
            os.makedirs(constant.DIR_IMAGE_STORAGE)

        file_name = self.save_image_data(request)
        image = self.save_image_info(request, file_name)

        start = datetime.datetime.now()
        person = None
        join = False
        while True:
            processed_image = models.Image.objects.get(id=image.id)
            if processed_image.status == models.Image.PENDING:
                time.sleep(0.1)
            else:
                person = processed_image.person
                session_persons = models.SessionPerson.objects.filter(person_id=person.id,
                                                                      session_id=request.data['session_id'])
                if len(session_persons) > 0:
                    join = True
                break

            if (datetime.datetime.now() - start).total_seconds() > 3:
                break

        if person == None or person.name == constant.UNKNOWN:
            result = [{"name": "unknown"}]
        else:
            result = [{"name": person.full_name,
                       "image_url": person.image_url,
                       "id": person.id,
                       "prob": processed_image.prob,
                       "joined": join,
                       }]

        return Response(result)

    def save_image_info(self, request, file_name):
        serializer = self.SERIALIZER_CLASS(data=request.data)
        if not serializer.is_valid():
            raise exceptions.ValidationError(serializer.errors)
        data = serializer.data

        try:
            session = models.Session.objects.get(id=data["session_id"])
        except models.Session.DoesNotExist:
            raise BaseAPIException()

        image = models.Image(name=file_name, session=session)
        image.save()

        return image

    def save_image_data(self, request):
        file = request.FILES['file']
        file_name = str(random.randint(1000000000000000, 999999999999999999))
        extension = ".png"

        with open('%s%s' % (constant.DIR_IMAGE_STORAGE, file_name + extension), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return file_name