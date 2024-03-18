from django.shortcuts import render
from LocationAlert.models import Locationalert
# Create your views here.
def setlocationalert_user(request):
    if request.method=='POST':
        obj=Locationalert()
        obj.user_id= 1
        obj.alert = request.POST.get('alert')
        obj.save()
    return render(request, 'LocationAlert/setlocationalalert_user.html')
def viewlocationbasedalert_user(request):
    obj = Locationalert.objects.all()
    context = {
        's': obj
    }
    return render(request, 'LocationAlert/viewlocationbasedalert_user.html',context)