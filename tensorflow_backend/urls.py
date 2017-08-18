"""tensorflow_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from tensorflow_backend.views import food_views, image_views, session_views, report_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^api/image/upload/', image_views.UploadView.as_view()),
    url(r'^api/recognition/notification/', image_views.ImageNotificationView.as_view()),
    url(r'^api/session/list_person/', session_views.PersonListView.as_view()),
    url(r'^api/session/person/confirm/', session_views.ConfirmView.as_view()),
    url(r'^api/food/order/get_by_user/', food_views.OrderInfoView.as_view()),

    url(r'^api/report/(?P<session_id>[0-9]+)/', report_views.ReportView.as_view()),
]
