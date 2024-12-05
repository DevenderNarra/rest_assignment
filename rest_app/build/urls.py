from django.urls import re_path

from rest_app.build.view_environments.todos_.router import todos_
from rest_app.build.view_environments.todos__id__.router import todos__id__


urlpatterns = [
    re_path(r'^todos/$', todos_),
    re_path(r'^todos/(?P<id>\d+)/$', todos__id__),
]