from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from football_arena.models import user_details,category,products,cart
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
import os




# Create your views here.

def start(request):
    var=category.objects.all()
    return render(request,'home.html',{'det':var})

def signin(request):
    var=category.objects.all()
    return render(request,'signin.html',{'det':var})

def signup(request):
    var=category.objects.all()
    return render(request,'signup.html',{'det':var})

@login_required(login_url='d_login')
def nav(request):
    return render(request,'nav2.html')

@login_required(login_url='d_login')
def cat(request):
    return render(request,'category.html')

@login_required(login_url='d_login')
def product(request):
    var=category.objects.all()
    return render(request,'add_product.html',{'cat':var})

@login_required(login_url='d_login')
def show_products(request):
    var=products.objects.all()
    return render(request,'show_products.html',{'det':var})

@login_required(login_url='d_login')
def user_detail(request):
    if request.user.is_authenticated:
        details=user_details.objects.all()
        return render(request,'user_detail.html',{'det':details})
    
@login_required(login_url='d_login')
def userhome(request):
    var=category.objects.all()
    return render(request,'userhome.html',{'cat':var})


def card(request,pk):
    var=category.objects.all()
    det=products.objects.filter(d_category=pk)
    return render(request,'card.html',{'det':det,'cat':var})
    

def register(request):
    if request.method =='POST':
        f_fname=request.POST['fname']
        f_sname=request.POST['sname']
        f_mail=request.POST['mail']
        f_user=request.POST['user']
        f_pwd1=request.POST['pwd1']
        f_pwd2=request.POST['pwd2']

        f_address=request.POST['address']
        f_number=request.POST['number']

        if f_pwd1 == f_pwd2:
            if User.objects.filter(username=f_user).exists():
                messages.info(request,'This username Already exists!!!')
                return redirect('signup')
            else:
                var=User.objects.create_user(
                    first_name=f_fname,
                    last_name=f_sname,
                    email=f_mail,
                    username=f_user,
                    password=f_pwd1
                )
                var.save()
                ff_user=User.objects.get(username=f_user)
                det=user_details(d_address=f_address,
                                 d_user=ff_user,
                                 d_number=f_number)
                det.save()
                messages.info(request,'Registration successfull')
                return redirect('start')
        else:
            messages.info(request,'Password Doesnot match')
            return redirect('signup')
    return redirect('signup')

def d_login(request):
    if request.method=='POST':
        f_user=request.POST['user']
        f_pwd=request.POST['pwd']
        var=auth.authenticate(username=f_user,password=f_pwd)
        if var is not None:
            if var.is_staff:
                login(request,var)
                return redirect('nav')
            else:
                login(request,var)
                # request.session['uid']=user.id         session method
                auth.login(request,var)
                messages.info(request,f'welcome  {f_user}')
                return redirect('userhome')
        else:
            messages.info(request,'invalid username or password.Try again')
            return redirect('signin')
    return render(request,'signin.html')

@login_required(login_url='d_login')
def add_category(request):
    if request.method=='POST':
        f_cat=request.POST['category']
        var=category(d_category=f_cat)
        var.save()
        messages.info(request,'Successfully Added')
        return redirect('cat')
    return redirect('cat')
        
@login_required(login_url='d_login')
def add_product(request):
     if request.method=='POST':
        f_p=request.POST['product']
        f_des=request.POST['description']
        f_price=request.POST['price']
        f_img=request.FILES['img']
        f_cat=request.POST['category']
        ff_cat=category.objects.get(id=f_cat)
        var=products(d_product=f_p,
                     d_description=f_des,
                     d_price=f_price,
                     d_img=f_img,
                     d_category=ff_cat)
        var.save()
        return redirect('product')
     return redirect('/')

@login_required(login_url='d_login')
def edit_product(request,pk):
    var=products.objects.get(id=pk)
    if request.method=='POST':
        var.d_price=request.POST['product']
        var.d_description=request.POST['description']
        var.d_price=request.POST['price']
        if len(request.FILES)!=0:
            if len(var.d_img)>0:
                os.remove(var.d_img.path)
            var.d_img=request.FILES['img']
        f_cat=request.POST['category']
        var.d_category=category.objects.get(id=f_cat)
        
        var.save()
        return redirect('show_products')

    return render(request,'edit_product.html',{'det':var})

@login_required(login_url='d_login')
def delete_product(request,pk):
    var=products.objects.get(id=pk)
    if var.d_img:
        var.d_img.delete()
    var.delete()
    return redirect('show_products')

@login_required(login_url='d_login')
def delete_user(request,pk):
    var=user_details.objects.get(id=pk)
    var.delete()
    var.d_user.delete()
    return redirect('user_detail')

@login_required(login_url='d_login')
def d_logout(request):
    logout(request)
    auth.logout(request)
    return redirect('start')

@login_required(login_url='d_login')
def add_to_cart(request,pk):
    current_user=request.user
    pro=products.objects.get(id=pk)

    var=cart(user=current_user,product=pro)
    var.save()
    return redirect('show_cart')

@login_required(login_url='d_login')
def show_cart(request):
    if cart.objects.filter(user=request.user).exists():
        cat=category.objects.all()
        var=cart.objects.all()
        return render(request,'cart.html',{'det':var,'cat':cat})
    else:
        messages.info(request,'Cart is Empty...')
    return redirect('userhome')

@login_required(login_url='d_login')
def delete_cart(request,pk):
    var=cart.objects.get(id=pk)
    var.delete()
    return redirect('show_cart')







