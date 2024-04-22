from django.shortcuts import render
from User.models import User
from login.models import Login
# Create your views here.
def post_user(request):
    if request.method=='POST':
        obj = User()
        obj.user=request.POST.get('user')
        obj.user_address=request.POST.get('address')
        obj.email=request.POST.get('Email')
        obj.user_number = request.POST.get('Number')
        obj.save()
        ob=Login()
        ob.username=obj.user
        ob.password= obj.user_number
        ob.type='user'
        ob.uid=obj.user_id
        ob.save()
    return render(request, 'User/post_user.html')