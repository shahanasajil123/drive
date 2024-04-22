from django.conf.urls import url
from Police import views

urlpatterns = [
url('policereg/', views.postnotification_police),
url('viewcomplaints_admin_police/', views.viewcomplaints_admin_police)
]