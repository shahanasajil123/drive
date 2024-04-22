from django.conf.urls import url
from Notification import views

urlpatterns = [
url('postnotification_police/', views.postnotification_police),
url('viewnotification_user/', views.viewnotification_user),
]