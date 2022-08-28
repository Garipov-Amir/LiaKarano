from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('/<int:pic_id>', views.picture, name='picture'),
]