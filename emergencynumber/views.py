from django.shortcuts import render
from emergencynumber.models import Emergencynumber


def  setemergencynumber_admin(request):
    if request.method=='POST':
        obj=Emergencynumber()
        obj.emergency_no = request.POST.get('emergencynumber')
        obj.save()
    return render(request, 'emergencynumber/setemergencynumber_admin.html')

def  viewEmergencynumber_user(request):
    obj = Emergencynumber.objects.all()
    context = {
        's': obj
    }
    return render(request, 'emergencynumber/setemergencynumber_admin.html',context)



