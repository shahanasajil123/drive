from django.shortcuts import render
from Police.models import Police
# Create your views here.
def postnotification_police(request):
    if request.method=='POST':
        obj=Police()
        obj.police_name = request.POST.get('police')
        obj.location = request.POST.get('location')
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('password')
        obj.save()
    return render(request, 'Police/postnotification_police.html')

def viewcomplaints_admin_police(request):
    obj = Police.objects.all()
    context = {
        's': obj
    }
    return render(request,'Police/viewcomplaints_admin_police.html',context)