from django.conf.urls import url
from DrowsinessReport import views

urlpatterns = [
url('policeviewdrowsinessreport/', views.policeviewdrowsinessreport),
url('viewdrowsinessalert_user/', views.viewdrowsinessalert_user),
url('adminviewdrowsiness/', views.adminviewdrowsiness),
url('hospitalviewdrowsiness/',views.hospitalviewdrowsiness),
]