from django.conf.urls import url

from . import views

app_name='analys'
urlpatterns = [
		url(r'^S',views.index,name='index'),
		]
