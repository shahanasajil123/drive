from django.shortcuts import render
from Notification.models import Notification

# Create your views here.
def postnotification_police(request):
    if request.method=='POST':
        obj=Notification()
        obj.notification= request.POST.get('notification_id')
        obj.police_id = 1
        obj.save()
    return render(request, 'Notification/postnotification_police.html')
def viewnotification_user(request):
    obj = Notification.objects.all()
    context = {
        's': obj
    }
    return render(request, 'Notification/viewnotification_user.html',context)
