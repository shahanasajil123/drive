from django.shortcuts import render
from SecondaryNumber.models import Secondarynumber

# Create your views here.
def secondarynumberandinform_hosoital(request):
    obj = Secondarynumber.objects.all()
    context = {
        's': obj
    }

    return render(request, 'SecondaryNumber/secondarynumberandinform_hospital.html',context)


def setsecondarynumber_admin(request):
    if request.method=='POST':
        obj=Secondarynumber()
        obj.number = request.POST.get('number')
        obj.user_id = 1
        obj.save()
    return render(request, 'SecondaryNumber/setsecondarynumber_admin.html')