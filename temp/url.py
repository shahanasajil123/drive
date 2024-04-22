from django.conf.urls import url
from temp import views

urlpatterns = [
    url('home/',views.home),
    url('admin/',views.adminhome),
    url('hospital/',views.hospitalhome),
    url('police/',views.policehome),
    url('user/',views.userhome),
]