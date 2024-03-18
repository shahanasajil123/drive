from django.shortcuts import render
from Dangerouslocation.models import  DangerousLocation
# Create your views here.

def dangerouslocation_admin(request):
    if request.method=='POST':
        obj=DangerousLocation()
        obj.location=request.POST.get('location')
        obj.save()
    return render(request, 'Dangerouslocation/dangerouslocation_admin.html')
