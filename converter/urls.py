from django.urls import path
from .views import ConverterView


urlpatterns = [
    path('convert/', ConverterView.as_view(), name='convert_currency'),
]
