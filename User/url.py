from django.conf.urls import url
from User import views

urlpatterns = [
    url('post_user/', views.post_user)
]