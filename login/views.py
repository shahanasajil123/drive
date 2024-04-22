from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.

def post_login(request):
  if request.method =="POST":
      uname = request.POST.get("uname")
      passw = request.POST.get("pwd")
      obj = Login.objects.filter(username=uname,password=passw)
      tp = ""
      for ob in obj :
          tp = ob.type
          uid = ob.uid
          if tp == "admin":
              request.session["u_id"] = uid
              objlist = "Login Successfully...!"
              context = {
                  'msg': objlist
              }
              return render(request,'temp/adminhome.html',context)
              # return HttpResponseRedirect('/temp/admin/',context)
          elif tp == "user":
              request.session["u_id"] = uid
              objlist = "Login Successfully...!"
              context = {
                  'msg': objlist
              }
              return render(request,'temp/userhome.html',context)
              # return HttpResponseRedirect('/temp/user/',context)
          elif tp == "police":
             request.session["u_id"] = uid
             objlist = "Login Successfully...!"
             context = {
                 'msg': objlist
             }
             return render(request,'temp/policehome.html',context)
             # return HttpResponseRedirect('/temp/police/',context)

      else:
          objlist = "username or password incorrect..... please try again.....!"
          context = {
               'msg': objlist
          }
          return render(request,'login/login.html',context)
  return render(request,'login/login.html')