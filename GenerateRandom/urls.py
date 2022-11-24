from django.contrib import admin
from django.urls import path,include
from GenerateRandom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('output',views.output,name='script')
]
