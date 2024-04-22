from django.conf.urls import  url
from Complaints import  views
urlpatterns=[
    url('post_complaint/', views.postcomplaints_user),
    url('complaint_status/',views.viewcomplaintsbypolice),
    url('vc_admin_police/',views.viewcomplaints_admin_police),
    url('viewcomplaintbypolice/',views.viewcomplaintsbypolice),
    url('postreply/(?P<idd>\w+)',views.postreply),
    url('complaint_status/',views.Complaintstatus_user),
]