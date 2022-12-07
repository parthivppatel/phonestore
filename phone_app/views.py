from django.shortcuts import render,redirect
from phone_app.models import mobile
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import math, random
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    realme=mobile.objects.filter(brand='realme')
    oppo=mobile.objects.filter(brand='oppo')
    vivo=mobile.objects.filter(Q(brand='vivo') |  Q(brand='redmi') | Q(brand='nokia'))[:5]
    plus=mobile.objects.filter(brand='plus')
    iphone=mobile.objects.filter(brand='iphone')
    
    lst_mobiles=[]
    lst_mobiles.append(realme)
    lst_mobiles.append(oppo)
    lst_mobiles.append(vivo)
    lst_mobiles.append(iphone)
    lst_mobiles.append(plus)

    return render(request,'index.html',{'object':lst_mobiles})

def cart(request):
    return render(request,'cart.html')


def login(request):
    if request.method == 'POST':
        u_name=request.POST['u_name']
        passwd=request.POST['pass']

        user=auth.authenticate(username=u_name,password=passwd)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,'Username or Password incorret')
            return redirect("login")
    else:
        return render(request,'sign_in.html')

def signup(request):
    return render(request,'sign_up.html')

def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        u_name=request.POST['u_name']
        email=request.POST['email']
        passw=request.POST['pass']
        re_passw=request.POST['re_pass']

        if passw == re_passw:
            if not User.objects.filter(username=u_name).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username=u_name,password=passw,first_name=name,email=email)
                    user.save()
                    return redirect("/")
                else:
                    messages.warning(request,'Email already exist...')
            else:
                messages.warning(request,'Username already exist, please try new one...')
            
        else:
            messages.warning(request,'Password not matches...')

    return render(request,'sign_up.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def email(request):
    if request.method=="POST":
        email=request.POST['email']
        name="Recovery Account"

        if email != "" and email is not None:
            digits = "0123456789"
            OTP = ""

            for i in range(6) :
              OTP += digits[math.floor(random.random() * 10)]
            
            message="Your OTP is " + OTP 

            send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
            ) 
        
            messages.success(request,"Email sent succesfully")
            context={
                'otp':[OTP],
                'email':[email]
            }
            return render(request,'otp.html',context)
        
        messages.error(request,"Please Enter valid Email")
        return render(request,"forgot.html")

    else:
        return redirect("/")
    

def forgot(request):
    return render(request,'forgot.html')


def reset(request):
    if request.method == 'POST':
        otp=request.POST['otp']
        user_otp=request.POST['user_otp']   
        email=request.POST['email']   
        if(otp == user_otp):
            return render(request,'reset.html',{'email':[email]})          
        else:
            messages.error(request,"Wrong OTP")
            return render(request,'otp.html')
    
    else:
        return redirect('/')

def password(request):
    if request.method == 'POST':
        passwd=request.POST['pass']
        cpasswd=request.POST['cpass']
        email=request.POST['email']
        print(type(passwd))
        print(type(cpasswd))
        print(email)

        if(passwd == cpasswd):
            user=User.objects.get(email=email)
            if user is not None:
                user.password=make_password(passwd)
                user.first_name="parthivv"
                user.save()

                auth.login(request,user)

                return redirect("/")
            else:
                messages.error(request,"User Not Found")
                return redirect('reset')
        else:
            messages.error(request,"password not matches")
            return render(request,'reset.html')
    else:
        return redirect("/")