from django.conf.urls import url
from HospitalReport import views

urlpatterns = [
url('add_report/', views.add_report),
url('view_report/', views.manage_report),
url('edit/(?P<idd>\w+)', views.updatereport_hospital),
url('user_vr/', views.reporthospital_user)
]