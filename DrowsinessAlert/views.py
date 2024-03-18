from django.shortcuts import render
from  DrowsinessAlert.models import  Drowsinessalert
# Create your views here.
def viewdrowsinssalert_user(request):
    if request.method=='POST':
        obj=Drowsinessalert()
        obj.alert=request.POST.get('alert')
        obj.save()

    return render(request, 'DrowsinessrAlert/viewdrowsinessalert_user.html')
