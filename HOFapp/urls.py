from django.conf.urls import include, url
from HOFapp import views

urlpatterns = [
    
    url(r'$^',     views.index, name='index'),
]