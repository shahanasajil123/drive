from django.conf.urls import url
from LocationAlert import views

urlpatterns = [
url('setlocationalert_user/', views.setlocationalert_user),
url('viewlocationbasedalert_user/', views.viewlocationbasedalert_user),

]