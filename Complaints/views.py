from django.shortcuts import render
from Complaints.models import Complaints
import datetime
# Create your views here.
def postcomplaints_user(request):
    if request.method=='POST':
        obj=Complaints()
        obj.complaint=request.POST.get('complaints')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.user_id=1
        obj.police_id=1
        obj.reply='pending'
        obj.save()
    return render(request, 'Complaints/postcomplaints_user.html')
def Complaintstatus_user(request):
    obj = Complaints.objects.filter(user_id=1)
    context = {
        's': obj
    }
    return render(request,'Complaints/complaintstatus_user.html', context)
def viewcomplaints_admin_police(request):
    obj = Complaints.objects.all()
    context = {
        's': obj
    }
    return render(request, 'Complaints/viewcomplaints_admin_police.html',context)
def postreply(request,idd):
    if request.method=="POST":
        ob=Complaints.objects.get(complains_id=idd)
        ob.reply=request.POST.get('Reply')
        ob.Police_id=1
        ob.save()
    return render(request, 'Complaints/postreply.html')
def viewcomplaintsbypolice(request):
    obj = Complaints.objects.all()
    context = {
        's': obj
    }
    return render(request, 'Complaints/viewcomplaintbypolice.html',context)

