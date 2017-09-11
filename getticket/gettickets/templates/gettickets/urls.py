from django.conf.urls import url

from . import views

app_name='gettickets'
urlpatterns = [
		url(r'^$',views.index,name='index'),
		url(r'^(?P<ticket_number>[0-9]+)/$',views.details,name='details'),
		]
