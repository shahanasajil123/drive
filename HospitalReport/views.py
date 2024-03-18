from django.shortcuts import render
from HospitalReport.models import Hospitalreport
# Create your views here.
def reporthospital_user(request):
    obj = Hospitalreport.objects.all()
    context = {
        's': obj
    }
    return render(request, 'HospitalReport/view_reporthospital_user.html', context)
def updatereport_hospital(request,idd):
    obj = Hospitalreport.objects.get(hospital_report_id=idd)
    context = {
        's': obj
    }
    if request.method=="POST":
        obj.report = request.POST.get('Report')
        obj.status = 'pending'
        obj.save()
    return render(request, 'HospitalReport/updatereport_hospital.html',context)
def add_report(request):
    if request.method=='POST':
        obj=Hospitalreport()
        obj.report = request.POST.get('Report')
        obj.status='pending'
        obj.save()
    return render(request, 'HospitalReport/add_report.html')
def manage_report(request):
    obj = Hospitalreport.objects.all()
    context = {
        's': obj
    }
    return render(request, 'HospitalReport/manage_report.html', context)
