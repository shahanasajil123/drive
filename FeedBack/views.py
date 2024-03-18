from django.shortcuts import render
from FeedBack.models import Feedback
import datetime
# Create your views here.
def  postfeedback_user(request):
    if request.method=='POST':
        obj=Feedback()
        obj.Feedback = request.POST.get('Feedback')
        obj.user_id=1
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request, 'FeedBack/postfeedback_user.html')
def  viewfeedback_admin(request):
    obj =Feedback .objects.all()
    context = {
        's': obj
    }
    return render(request, 'FeedBack/viewfeedback_admin.html',context)

