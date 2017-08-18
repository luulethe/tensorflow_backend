import datetime

from tensorflow_backend import serializers, models, constant
from tensorflow_backend.views.base_views import BaseAPIView


class PersonListView(BaseAPIView):
    SERIALIZER_CLASS = serializers.SessionListSerializer

    def process(self, data):
        session_person_list = list(models.SessionPerson.objects.filter(session_id=data["session_id"]))
        person_map = {session_person.person_id: session_person for session_person in session_person_list}
        result = []

        person_ids = [session_person.person_id for session_person in session_person_list]
        person_list = models.Person.objects.filter(id__in=person_ids)

        for p in person_list:
            if p.name != constant.UNKNOWN:
                session = person_map.get(p.id)
                result.append({
                    "name": p.name,
                    "id": p.id,
                    "image_url": p.image_url,
                    "check_time": session.time
                })

        return result


class ConfirmView(BaseAPIView):
    SERIALIZER_CLASS = serializers.ConfirmSerializer

    def process(self, data):
        try:
            session_person, created = models.SessionPerson.objects.get_or_create(person_id=data["user_id"],
                                                                                 session_id=data["session_id"])
            session_person.time = datetime.datetime.now()
            session_person.save()
        except:
            return {"error": "ERROR"}
        return {"error": "OK"}