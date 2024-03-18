from django.shortcuts import render
from User.models import User
# Create your views here.
def post_user(request):
    if request.method=='POST':
        obj = User()
        obj.user=request.POST.get('user')
        obj.user_address=request.POST.get('address')
        obj.email=request.POST.get('Email')
        obj.number = request.POST.get('Number')
        obj.save()
    return render(request, 'User/post_user.html')