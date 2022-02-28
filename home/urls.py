from django.urls import path,include 
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    # path('stream/',include(streamapp.urls),name='stream'),
]