from django.shortcuts import render
from DrowsinessReport.models import Drowsinessreport
# Create your views here.
def viewdrowsinessalert_user(request):
    if request.method=='POST':
        obj=Drowsinessreport()
        obj.alert = request.POST.get('alert')
        obj.save()
    return render(request, 'DrowsinessReport/viewdrowsinessalert_user.html')



def policeviewdrowsinessreport(request):
    obj = Drowsinessreport.objects.all()
    context = {
        's': obj
    }
    return render(request, 'DrowsinessReport/policeviewdrowsinessreport.html',context)
def adminviewdrowsiness(request):
    obj = Drowsinessreport.objects.all()
    context = {
        's': obj
    }
    return render(request, 'DrowsinessReport/adminviewdrowsiness.html',context)
def hospitalviewdrowsiness(request):
    obj = Drowsinessreport.objects.all()
    context = {
        's': obj
    }
    return render(request, 'DrowsinessReport/hospitalviewdrowsinessreport.html',context)