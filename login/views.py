from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

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
            return render(request, 'home.html')
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
        dup_user = User.objects.all().filter(email = Email)
        flg = True
        for x in dup_user:
            if x.email == Email:
                flg=False
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
