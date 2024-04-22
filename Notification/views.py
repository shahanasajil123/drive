from django.shortcuts import render
from Notification.models import Notification

# Create your views here.
def postnotification_police(request):
    uid=request.session["u_id"]
    if request.method=='POST':
        obj=Notification()
        obj.notification= request.POST.get('notification')
        obj.police_id = uid
        obj.save()
    return render(request, 'Notification/policenotification.html')
def viewnotification_user(request):
    obj = Notification.objects.all()
    context = {
        's': obj
    }
    return render(request, 'Notification/viewnotification_user.html',context)
