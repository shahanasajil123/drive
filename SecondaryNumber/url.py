from django.conf.urls import url
from SecondaryNumber import views

urlpatterns = [
url('secondarynumberandinform_hospital/', views.secondarynumberandinform_hosoital),
url('admin/', views.setsecondarynumber_admin)]