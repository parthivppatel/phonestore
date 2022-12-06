from django.shortcuts import render
from phone_app.models import mobile
from django.db.models import Q

# Create your views here.
def home(request):
    realme=mobile.objects.filter(brand='realme')
    oppo=mobile.objects.filter(brand='oppo')
    vivo=mobile.objects.filter(Q(brand='vivo') |  Q(brand='redmi') | Q(brand='nokia'))[:5]
    # nokia=mobile.objects.filter(brand='nokia')
    # redmi=mobile.objects.filter(brand='redmi')
    plus=mobile.objects.filter(brand='plus')
    iphone=mobile.objects.filter(brand='iphone')
    
    lst_mobiles=[]
    lst_mobiles.append(realme)
    lst_mobiles.append(oppo)
    lst_mobiles.append(vivo)
    # lst_mobiles.append(nokia)
    # lst_mobiles.append(redmi)
    lst_mobiles.append(iphone)
    lst_mobiles.append(plus)
    # lst_mobiles.update({'vivo':vivo})
    # lst_mobiles.update({'nokia':nokia})
    # lst_mobiles.update({'redmi':redmi})
    # lst_mobiles.update({'plus':plus})
    # lst_mobiles.update({'iphone':iphone})

    # print(lst_mobiles)

    return render(request,'index.html',{'object':lst_mobiles})

def cart(request):
    return render(request,'cart.html')
