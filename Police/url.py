from django.conf.urls import url
from Police import views

urlpatterns = [
url('postnotification_police/', views.postnotification_police),
url('viewcomplaints_admin_police/', views.viewcomplaints_admin_police)
]