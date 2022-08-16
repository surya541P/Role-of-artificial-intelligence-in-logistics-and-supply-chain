from django.shortcuts import render
from users.forms import UserRegistrationForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def logout(request):
    return render(request, 'index.html', {})


def UserLogin(request):
    return render(request, 'UserLogin.html', {})


def UserRegister(request):
    form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})

def Viewdata(request):
    import os
    import pandas as pd
    from django.conf import settings
    path = os.path.join(settings.MEDIA_ROOT,'SeriesReport-Not Seasonally Sales.csv')
    df = pd.read_csv(path)
    print(df)
    df = df.to_html()
    return render(request, 'users/Viewdata.html', {'data': df})
