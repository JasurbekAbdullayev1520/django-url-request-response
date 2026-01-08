from django.urls import path

from .views import home_view, get_user_by_id_view
from .views import calculators_view


urlpatterns = [
    path('home/', home_view),
    path('<int:id>', get_user_by_id_view),
    path('calculators',calculators_view)
]
