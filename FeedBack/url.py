from django.conf.urls import url
from FeedBack import views

urlpatterns = [
    url('postfeedback_user/', views.postfeedback_user),
    url('viewfeedback_admin/', views.viewfeedback_admin),
]