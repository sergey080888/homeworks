from django.urls import path

from measurement.views import SensorIdView, SensorList, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorList.as_view()),
    path('sensors/<pk>', SensorIdView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
