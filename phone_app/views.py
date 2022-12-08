from django.shortcuts import render,redirect
from phone_app.models import mobile
from phone_app.models import cart as cart_
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import math, random
from django.contrib.auth.hashers import make_password
from phone_app.models import profile
from datetime import datetime
cart_ids=[]
count_cart = 0

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
    
    if request.user.id != None:
        data=cart_.objects.filter(Q(user=request.user) & Q(is_order=False)).select_related('product')

        global count_cart
        count_cart=len(data)

    context={
        'object':lst_mobiles,
        'count_cart':[count_cart]
    }

    return render(request,'index.html',context)

def cart(request,id=0):
    global count_cart
    if request.method=="POST":
        user_id=request.user
        product_id=id
        # print("id",user_id)
        # print("product",product_id)

        now=datetime.today().date()
        cart_ids.append(product_id)
        for i in cart_ids:
            if not cart_.objects.filter(Q(user=user_id) &  Q(product=i)).exists():
                # print(i)
                ref=mobile(id=i)
                products=cart_(user=user_id,product=ref,is_order=False,quantity=1,date=now)
                products.save()

        data=cart_.objects.filter(Q(user=user_id) & Q(is_order=False)).select_related('product')

        count_cart=len(data)

        context={
            'data':data,
            'count_cart':[count_cart]
        }

        # print(cart_ids)
        return render(request,'cart.html',context)
    else:
        data=cart_.objects.filter(Q(user=request.user) & Q(is_order=False)).select_related('product')

        # global count_cart
        count_cart=len(data)

        context={
            'data':data,
            'count_cart':[count_cart]
        }
        return render(request,'cart.html',context)


def login(request):
    if request.method == 'POST':
        u_name=request.POST['u_name']
        passwd=request.POST['pass']

        user=auth.authenticate(username=u_name,password=passwd)

        if user is not None:
            auth.login(request,user)
            global cart_ids
            cart_ids=[]
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
                    auth.login(request,user)
                    global cart_ids
                    cart_ids=[]
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

def remove(request):
    if request.method == 'POST':
       prd_id=request.POST['prd_id']
       ref=mobile(id=prd_id)
       cart_remove=cart_.objects.filter(Q(product=ref) & Q (user=request.user))
       cart_remove.delete()

    data=cart_.objects.filter(Q(user=request.user) & Q(is_order=False)).select_related('product')
    count_cart=len(data)

    context={
        'data':data,
        'count_cart':[count_cart]
    }
    return render(request,'cart.html',context)

def clear(request):
    if request.method == "POST":
       cart_remove=cart_.objects.filter(user=request.user)
       cart_remove.delete()

       data=cart_.objects.filter(Q(user=request.user) & Q(is_order=False))
       count_cart=len(data)

       context={
        'data':data,
        'count_cart':[count_cart]
        }

       return render(request,'cart.html',context)
        
    else:
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
            context={
                'email':[email],
                'otp':[user_otp]
            }
            return render(request,'otp.html',context)
    
    else:
        return redirect('/')

def password(request):
    if request.method == 'POST':
        passwd=request.POST['pass']
        cpasswd=request.POST['cpass']
        emails=request.POST['emails']

        if(passwd == cpasswd):
            user=User.objects.get(email=emails)
            if user is not None:
                user.password=make_password(passwd)
                user.save()

                auth.login(request,user)
                global cart_ids
                cart_ids=[]

                return redirect("/")
            else:
                messages.error(request,"User Not Found")
                return redirect('reset')
        else:
            messages.error(request,"password not matches")
            return render(request,'reset.html',{'email':[emails]})
    else:
        return redirect("/")