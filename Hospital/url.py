from django.conf.urls import url
from Hospital import views

urlpatterns = [
url('hospital_reg/', views.hospital_reg),
url('viewhospital_reg/', views.viewhospital_reg)
]