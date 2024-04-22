from django.shortcuts import render
from  DrowsinessAlert.models import  Drowsinessalert
# Create your views here.
def viewdrowsinssalert(request):
    ob=Drowsinessalert.objects.all()
    context={
        'x':ob
    }
    return render(request, 'DrowsinessrAlert/viewdrowsinessalert_user.html',context)
