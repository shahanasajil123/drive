from django.conf.urls import url
from emergencynumber import views

urlpatterns = [
        url('set/', views.setemergencynumber_admin),
        url('viewemergencynumber_user/', views.viewEmergencynumber_user),

]