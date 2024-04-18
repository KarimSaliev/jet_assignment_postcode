from django.urls import path
from main.views import index, fetch_data
app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('postcode/<str:postcode>/', fetch_data, name='fetch_data')
]