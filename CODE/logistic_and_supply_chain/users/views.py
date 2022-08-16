from django.shortcuts import render

from users.algorithm.ProcessAlgorithm import Algorithms
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import UserRegistrationModel

algo = Algorithms()


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(
                loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(
                    request, 'Your Account has not been activated by Admin.')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def Arma(request):
    pred_ci, ax = algo.stat_predation()

    pred_ci = pred_ci.to_html

    return render(request, "users/Arma.html", {"x": pred_ci, "y": ax})


def viewdata(request):
    import os
    import pandas as pd
    from django.conf import settings
    import seaborn as sns
    import matplotlib.pyplot as plt

    path = os.path.join(settings.MEDIA_ROOT,
                        'SeriesReport-Not Seasonally Sales.csv')
    df = pd.read_csv(path)
    print(df)

    ax = df.plot.bar(x='Period', y='Value', figsize=(15, 14))
    plt.show()

    df = df.to_html()

    return render(request, 'admins/adminviewdata.html', {'data': df, "x": ax})
