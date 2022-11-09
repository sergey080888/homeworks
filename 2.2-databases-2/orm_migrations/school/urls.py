from django.conf.urls.static import static
from django.urls import path, include
from website import settings

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
]

