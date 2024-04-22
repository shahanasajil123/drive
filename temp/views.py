from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'temp/home.html')
def adminhome(request):
    return render(request, 'temp/adminhome.html')
def hospitalhome(request):
    return render(request, 'temp/hospitalhome.html')
def policehome(request):
    return render(request, 'temp/policehome.html')
def userhome(request):
    return render(request, 'temp/userhome.html')
