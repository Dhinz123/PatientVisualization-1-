from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('patient/', views.patient_detail, name='patient_detail'),
    # path('detail/', views.patient_detail, name='patient_detail'),
]