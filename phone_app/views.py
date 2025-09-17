from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from phone_app.models import mobile
from phone_app.models import cart as cart_
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import math, random
from django.contrib.auth.hashers import make_password
from phone_app.models import profile ,orders,card
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db.models import Sum, F, IntegerField, ExpressionWrapper


# Helpers
def get_cart_queryset(user, is_order=False):
    return cart_.objects.filter(user=user, is_order=is_order).select_related('product')


def get_cart_count(user):
    try:
        return get_cart_queryset(user, is_order=False).count()
    except Exception:
        return 0


def render_with_cart(request, template_name, extra_context=None):
    context = {'count_cart': [get_cart_count(request.user)]}
    if extra_context:
        context.update(extra_context)
    return render(request, template_name, context)


def get_order_context(user, shipping_fee=40):
    qs = get_cart_queryset(user, is_order=False)
    subtotal = qs.aggregate(total=Sum('subtotal'))['total'] or 0
    count = qs.count()
    return {
        'order_data': qs,
        'total': [subtotal + shipping_fee],
        'subtotal': [subtotal],
        'count': [count]
    }

# Create your views here.
def home(request):
    realme=mobile.objects.filter(brand='realme')
    oppo=mobile.objects.filter(brand='oppo')
    vivo=mobile.objects.filter(Q(brand='vivo') |  Q(brand='redmi') | Q(brand='nokia') | Q(brand='plus'))
    # plus=mobile.objects.filter(brand='plus')
    iphone=mobile.objects.filter(brand='iphone')

    lst_mobiles=[]
    lst_mobiles.append(realme)
    lst_mobiles.append(oppo)
    lst_mobiles.append(vivo)
    lst_mobiles.append(iphone)
    # lst_mobiles.append(plus)
    
    context={
        'object':lst_mobiles
    }

    return render_with_cart(request,'index.html',context) 

@login_required
@require_POST
def delete(request):
    user=User.objects.filter(id=request.user.id)
    user.delete()
    auth.logout(request)
    messages.success(request,"Account Deleted Succesfully")
    return HttpResponseRedirect(reverse('home'))

@login_required
def prof(request):
    if request.method== "POST":
        
        uname=request.POST['user']
        fname=request.POST['fname']
        email=request.POST['email']
        phone=request.POST['phone']
        pincode=request.POST['pincode']
        landmark=request.POST['landmark']
        city=request.POST['city']
        flat=request.POST['flat']
        area=request.POST['area']
        country=request.POST['country']
        state=request.POST['state']

        check_uname=User.objects.filter(username=uname).exclude(username=uname,id=request.user.id)
        data=profile.objects.filter(user=request.user)
        
        if not check_uname:
            check_email=User.objects.filter(email=email).exclude(email=email,id=request.user.id)
            if not check_email:
                check_phone=profile.objects.filter(phone=phone).exclude(phone=phone,user=request.user)
                if not check_phone:
                   data=profile.objects.get(user=request.user)
                   data.phone=phone
                   data.landmark=landmark
                   data.city=city
                   data.flat=flat
                   data.area=area
                   data.state=state
                   data.country=country 
                   data.pincode=pincode 
                   data.save()    

                   user_data=User.objects.get(id=request.user.id)
                   user_data.username=uname
                   user_data.first_name=fname
                   user_data.email=email
                   user_data.save()

                   messages.success(request,"Profile Updated Succesfully")
                   return HttpResponseRedirect(reverse('home'))
                else:
                    messages.warning(request,'Phone no alreay exist...')
                    return render_with_cart(request,'profile.html',{'data':data})
            else:
                messages.warning(request,'Email already exist...')
                return render_with_cart(request,'profile.html',{'data':data})

            
        else:
            messages.warning(request,'Username already exist...')
            return render(request,'profile.html',{'data':data})
            
    else:    
        if(request.user.id!=None): 
            data=profile.objects.filter(user=request.user).select_related('user')
            return render_with_cart(request,'profile.html',{'data':data})
        else:
            return redirect("/")
    

@login_required
@require_POST
def next(request):
        for i in request.POST:
            if i != "csrfmiddlewaretoken":
                # print(i)
                name=i.split("_")[0]
                if(name=="quantity"):
                   prod_id=i.split("_")[1]
                   prod_q=request.POST[f"quantity_{prod_id}"]

                #    print("....",prod_id)
                    
                   if int(prod_q)>=1:
                       ref=mobile(id=prod_id)
                    #    print("------",ref)
                       quan_ad=cart_.objects.get(Q(product=ref) & Q (user=request.user) & Q(is_order= False))
                       quan_ad.quantity=prod_q
                       quan_ad.save()
                  
                   ref=mobile(id=prod_id)
                   sub=cart_.objects.filter(Q(product=ref) & Q (user=request.user) & Q(is_order= False)).select_related('product')  

                #    print(len(sub))      

                   for i in sub:
                      subtotal=i.product.price*int(prod_q)
                    #   ref=mobile(id=prod_id)
                      obj=cart_.objects.get(Q(product=ref) & Q (user=request.user) & Q(is_order= False))
                      obj.subtotal=subtotal
                      obj.save()

                    
                elif(name=="delete"):
                    prod_id=i.split("_")[1]
                    prod_q=request.POST[f"delete_{prod_id}"]

                #    print("-----------------------------delete ",prod_id,prod_q)
                   
                    if prod_q=="true":
                        ref=mobile(id=prod_id)
                        cart_remove=cart_.objects.filter(Q(product=ref) & Q (user=request.user) & Q(is_order=False))
                        cart_remove.delete()
                        
                        data=get_cart_queryset(request.user, is_order=False)
                        context={
                        'data':data
                        }

                        return render_with_cart(request,'cart.html',context)          

        
        address=profile.objects.filter(Q(Q(phone=None) | Q(phone="") |( Q(country=None) | Q(country="")) | Q(state=None) | Q(state="")
        | Q(city=None) | Q(city="") | Q(area=None) | Q(area="") | Q(flat=None) | Q(flat=""))& Q(user=request.user))

        if address:
            data_=profile.objects.filter(user=request.user).select_related('user')
 
            # print("----------",i)
            return render_with_cart(request,'address.html',{'data':data_})

        else:
            context=get_order_context(request.user)
            return render_with_cart(request,"order.html",context)

        


@login_required
@require_POST
def order(request):
        
        phone=request.POST['phone']
        pincode=request.POST['pincode']
        landmark=request.POST['landmark']
        city=request.POST['city']
        flat=request.POST['flat']
        area=request.POST['area']
        country=request.POST['country']
        state=request.POST['state']

        check_phone=profile.objects.filter(phone=phone).exclude(phone=phone,user=request.user)
        if not check_phone:
            data=profile.objects.get(user=request.user)
            data.phone=phone
            data.landmark=landmark
            data.city=city
            data.flat=flat
            data.area=area
            data.state=state
            data.country=country  
            data.pincode=pincode
            data.save()    

            context=get_order_context(request.user)
            return render_with_cart(request,"order.html",context)
            
        else:
            data_=profile.objects.filter(user=request.user).select_related('user')
            messages.warning(request,'Phone no alreay exist...')
            return render_with_cart(request,'address.html',{'data':data_})

    
    

@login_required
@require_POST
def place(request):
        name=request.POST['name']
        number=request.POST['number']
        expiry=request.POST['expiry']
        cvv=request.POST['cvv']
        nums=["0","1","2","3","4","5","6","7","8","9"]
        
        # print("......first",number)
        check_number=card.objects.exclude(user=request.user).filter(number=number)
        if not check_number:
            check=False
            for i in number:
                # print("------i",i)
                if i not in nums:
                   check=True 
            # print(check)
            if check==True:
                messages.error(request,"Please Enter Valid Card Number")
                context=get_order_context(request.user)
                return render_with_cart(request,"order.html",context)
            else:
                data=card.objects.filter(user=request.user)   
                if not data:
                  create=card(name=name,number=number,expiry=expiry,cvv=make_password(cvv),user=request.user)
                  create.save()

                else:
                   data_update=card.objects.get(user=request.user)   
                # print("......first",number)
                   data_update.name=name   
                   data_update.number=number   
                   data_update.expiry=expiry  
                   data_update.cvv=make_password(cvv)
                   data_update.save()
        else:
            messages.error(request,"card number already exist")
            context=get_order_context(request.user)
            return render_with_cart(request,"order.html",context)
        
        now=timezone.now().date()
        status='pending'



        carts=cart_.objects.filter(Q(is_order=False) & Q(user=request.user)).select_related('product')

        for i in carts:
            ref_cart=cart_(id=i.id)
            ref_product=mobile(id=i.product.id)
            check_order=orders.objects.filter(cart=ref_cart)
            if not check_order:
                order_data=orders(date=now,status=status,quantity=i.quantity,cart=ref_cart,product=ref_product,total=i.subtotal,user=request.user)
                order_data.save()
                is_order=cart_.objects.get(id=i.id)
                is_order.is_order=True
                is_order.save()
                # print("==============",i.id)

        messages.success(request,"your order has been placed succesfully")
        return HttpResponseRedirect(reverse('home'))

    

@login_required
def your(request):
        if(request.user.id!=None):
            your_data=cart_.objects.filter(Q(user=request.user) & Q(is_order=True)).select_related('product')

            # global count_cart
            count_cart=len(your_data)

            context={
              'data':your_data,
              'count_cart':[count_cart]
            }
            return render(request,'orders.html',context)
        else:
            return redirect("/")


@login_required
def cart(request,id=0):
    if request.method=="POST":
        user_id=request.user
        product_id=id

        # print("id",user_id)
        # print("product",product_id)
        # print(cart_ids," before cart_ids")
        now=timezone.now().date()
        ref=mobile(id=product_id)
        if not cart_.objects.filter(Q(user=request.user) &  Q(product=ref) & Q(is_order=False)):
            products=cart_(user=user_id,product=ref,is_order=False,quantity=1,date=now)
            products.save()

        data=get_cart_queryset(user_id, is_order=False)

        context={
            'data':data
        }

        return render_with_cart(request,'cart.html',context)
    else:
        data=get_cart_queryset(request.user, is_order=False)

        context={
          'data':data
        }
        return render_with_cart(request,'your_order.html',context)


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
                    profile_=profile(user=user,area='',phone='',country='',state='',city='',flat='',landmark='',pincode='')
                    user.save()
                    profile_.save()
                    auth.login(request,user)
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

@login_required
@require_POST
def clear(request):
       cart_remove=cart_.objects.filter(Q(user=request.user) & Q(is_order=False))
       cart_remove.delete()

       data=get_cart_queryset(request.user, is_order=False)

       context={
        'data':data
        }

       return render_with_cart(request,'cart.html',context) 
    

@require_POST
def email(request):
        email=request.POST['email']
        name="Recovery Account"
        
        check=User.objects.filter(email=email)
        if check:
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
        
        messages.error(request,"User Not Found")
        return render(request,"forgot.html")
    
    

def forgot(request):
    return render(request,'forgot.html')


def reset(request):
    if request.method == 'POST':
        otp=request.POST['otp']
        user_otp=request.POST['user_otp'] 
        email=request.POST['email']   
        if(otp == user_otp):
            messages.success(request,'OTP matches succesfully')
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

@require_POST
def password(request):
        passwd=request.POST['pass']
        cpasswd=request.POST['cpass']
        emails=request.POST['emails']

        if(passwd == cpasswd):
            user=User.objects.get(email=emails)
            if user is not None:
                user.password=make_password(passwd)
                user.save()

                auth.login(request,user)
                
                messages.success(request,"Password Updated Succesfully")
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request,"User Not Found")
                return redirect('reset')
        else:
            messages.error(request,"password not matches")
            return render(request,'reset.html',{'email':[emails]})