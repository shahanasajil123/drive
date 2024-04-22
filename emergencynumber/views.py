from django.shortcuts import render
from emergencynumber.models import Emergencynumber


def  setemergencynumber_admin(request):
    if request.method=='POST':
        obj=Emergencynumber()
        obj.emergency_no = request.POST.get('emergency_no')

        obj.save()
    return render(request, 'emergencynumber/setEmergencynumber_user.html')

def  viewEmergencynumber_user(request):
    obj = Emergencynumber.objects.all()
    context = {
        's': obj
    }
    return render(request, 'emergencynumber/viewemergencynumber_admin.html', context)



