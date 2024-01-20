from django.shortcuts import render,redirect
from .forms import*
from. models import*
from django.contrib.auth import logout
from django.core.mail import send_mail
from batchproject import settings
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
otp=random.randrange(1111,9999)

def index(request):
    msg=""
    user=request.session.get('firstname')
    if request.method=='POST':
        if request.POST.get("signup")=='signup':
            user=sign(request.POST) 
            if user.is_valid():
                username=user.cleaned_data.get("username")
                try:
                    usersingup.objects.get(username=username)
                    print("username is already exists")
                    msg="Username is already exists!"

                except usersingup.DoesNotExist:
                    user.save()
                    print("saved")
                    return redirect("notes")
            else:
                msg="Error!Something went wrong...."
                print(user.errors)

        elif request.POST.get("login")=='login':
            unm=request.POST['username']
            pwd=request.POST['password']

            data=usersingup.objects.filter(username=unm,password=pwd)
            fnm=usersingup.objects.get(username=unm)
            uid=usersingup.objects.get(username=unm)
           
            if data:
                print("login successfully...")
                request.session['user']=unm
                request.session['firstname']=fnm.firstname
                request.session['uid']=uid.id
                return redirect("notes")

            else:
                print("invalid username or password")
                msg='invalid username or password'
    return render(request,'index.html',{'user':user,'msg':msg})

def about(request):
     user=request.session.get("user")
     return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get("user")
    if request.method=='POST':
        data=feedbackform(request.POST)
        if data.is_valid():
            data.save()
            print("saved")
           
           
            sub='thank you'
            msg=f"Dear {request.POST['name']}!\n\nThanks for your feedback,\n your one time otp is {otp} we will connect shortly!\n\nIf any queries regarding, you can contact us\n\n+91 9724799469 | help@tops-int.com\n\nThanks & Regards!\nTOPS Tech - Rajkot\nwww.tops-int.com"
            fr=settings.EMAIL_HOST_USER
            re=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=fr,recipient_list=re,)
            return redirect("verification")
    
           

        else:
            print(data.errors)
    return render(request,'contact.html',{'user':user})

def notes(request):
    data=request.session.get("user")
    if request.method=='POST':
        user=nots(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            print("saved")
        else:
            print(user.errors)

    return render(request,'notes.html',{'data':data})
@ login_required
def profile(request):
    data=request.session.get("user")
    uid=request.session.get('uid')
    cuser=usersingup.objects.get(id=uid)
    if request.method=='POST':
        dat=sign(request.POST,instance=cuser)
        if dat.is_valid():
            dat.save()
            return redirect("notes")
        else:
            print(dat.errors)
    return render(request,'profile.html',{'data':data,'cuser':cuser})

def userlogout(request):
    logout(request)
    return redirect("/")


def verification(request):
    if request.method=='POST':
        if request.POST['otp_no']==str(otp):
            print(otp)
            return redirect("/")
        else:
            print('errors')
    return render(request,'verification.html')
