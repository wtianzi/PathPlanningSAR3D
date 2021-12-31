from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from pathplan.views import BaseTemplate,PathPlan3D
from django.views.generic import TemplateView

urlpatterns = [
    path('', BaseTemplate.as_view(), name='index'),
    path('pathsar_3d', PathPlan3D.as_view(), name='pathsar_3d'),
    path('test',TemplateView.as_view(template_name="pathplan/esritesting.html"),name="test"),

    url(r'^getpath$',PathPlan3D.getpath,name='getpath'),
]
