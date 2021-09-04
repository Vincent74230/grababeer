from django.urls import path
from . import views


app_name = "home"
urlpatterns = [
	path('', views.index, name='index'),
	path('save_my_beer', views.save_favourite, name='save_fav'),
]
