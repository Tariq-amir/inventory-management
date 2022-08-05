from itertools import product
from xml.etree.ElementTree import tostring

from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from inventory.forms import ProductForm
from inventory.models import Product
from pyuca import Collator
from django.db import connections

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.POST)
        print(form)
        if form.is_valid():
            tender_no = form.cleaned_data['tender_no']
            name = form.cleaned_data['name']
            model = form.cleaned_data['model']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            date_of_buy = form.cleaned_data['date_of_buy']
            alloted = form.cleaned_data['alloted']
            room = form.cleaned_data['room']
            month_year = str(date_of_buy)[0:7]
            product = Product(tender_no=tender_no, name=name, model=model, quantity=quantity,
                              price=price, date_of_buy=date_of_buy, alloted=alloted, room=room, month_year=month_year)
            product.save()
    form = ProductForm()
    return render(request, 'home.html', {'form': form})


def dashboard(request):
    result = Product.objects.raw(
        "select id,month_year,sum(price) as total from inventory_product where year='2022' group by month_year  order by month_year asc")
    expense = []
    y=0
    for x in range(12):
        month=0
        try:
            month = str(result[y].month_year)[5:]
        except:
            month=13
        month_expense={}
        if x == int(month)-1:
            month_expense = {
                str(x+1): result[y].total,
            }
            y+=1
        else:
            month_expense = {
                str(x+1): 0,
            }

        expense.append(month_expense)
    print(expense)
    products = Product.objects.all().order_by('name')
    # for product in products:
    #     if product.room=='gd':
    #         product.room
    context = {
        'products': products,
        'expense': expense,
    }
    return render(request, 'dashboard.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')


def base(request):
    return render(request, 'base.html')


def signin(request):
    if request.method == 'POST':
        username1 = request.POST['username1']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=username1, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            form = ProductForm()
            return redirect('home/', {'form': form})
        else:
            messages.error(request, "User email or password is wrong!")
            return redirect('signin')

    else:
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        Email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
# check for errorenous inputs
        if len(username) > 10:
            messages.error(
                request, "Maximum length of username is 10  characters.")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Invalid username!")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

# create the user
        dup_user = User.objects.all().filter(email=Email)
        flg = True
        for x in dup_user:
            if x.email == Email:
                flg = False
                break

        if flg == True:
            myuser = User.objects.create_user(username, Email, pass1)

            myuser.save()

            messages.success(
                request, 'Your account has been successfully created!')

            return redirect('signin')
        else:
            messages.error(request, "Email already used!")
            return redirect('signup')

    return render(request, 'signup.html')
