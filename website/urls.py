from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('location',views.location, name='location'),
    path('Predict',views.predict,name='predict'),
    path('Predict/DPF',views.dpf,name='dpf'),
    path('Predict/DPF/Family_Input',views.family,name='family'),
    path('Ml_Model',views.ml_model,name='ml_model')
]
