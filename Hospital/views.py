from django.shortcuts import render
from Hospital.models import Hospital
# Create your views here.
def hospital_reg(request):
    if request.method=='POST':
        obj=Hospital()
        obj.contact_number = request.POST.get('number')
        obj.hospital_name = request.POST.get('hospitalname')
        obj.address = request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.location=request.POST.get('location')
        obj.save()
    return render(request, 'Hospital/hospital_reg.html')
def viewhospital_reg(request):
    obj = Hospital.objects.all()
    context = {
        's': obj
    }
    return render(request, 'Hospital/hospital_reg.html',context)