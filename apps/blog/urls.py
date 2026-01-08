from django.urls import path

from django.urls import path
from .views import get_blogs_by_uuid_view


urlpatterns = [
    path('<uuid:id>', get_blogs_by_uuid_view),
]