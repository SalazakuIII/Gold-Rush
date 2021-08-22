from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('display', views.display),
    path('process_gold', views.process),
    path('reset', views.delete_session_data)

]