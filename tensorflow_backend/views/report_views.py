from django.shortcuts import render
from django.template import context
from django.views import View
from django.views.generic import FormView

from tensorflow_backend import models, constant


class ReportView(FormView):
    template_name = 'tensorflow_backend/report.html'

    def get(self, request, session_id):
        session_person_list = list(models.SessionPerson.objects.filter(session_id=session_id))
        person_map = {session_person.person_id: session_person for session_person in session_person_list}

        person_ids = [session_person.person_id for session_person in session_person_list]
        person_list = models.Person.objects.filter(id__in=person_ids)

        object_list = []
        for p in person_list:
            if p.name != constant.UNKNOWN:
                session = person_map.get(p.id)
                object_list.append({
                    "name": p.full_name,
                    "id": p.id,
                    "image_url": p.image_url,
                    "time": session.time
                })

        context = {"object_list": object_list}
        return render(request, self.template_name, context)