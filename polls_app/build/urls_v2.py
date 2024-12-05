from django.conf.urls import include
from django.urls import re_path



base_path = "api/polls_app/"

api_paths = [
]


urlpatterns = [
    re_path(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
