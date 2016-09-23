from django.conf.urls import url

from persons.views import delete_persons, list_persons, update_persons


urlpatterns = [
    url(r'^create$', update_persons, name='create'),
    url(r'^update/(?P<person_id>\d+)$', update_persons, name='update'),
    url(r'^delete/(?P<person_id>\d+)$', delete_persons, name='delete'),
    url(r'^$', list_persons, name='list'),
]
