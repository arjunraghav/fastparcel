from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.
def home(request):
    return render(request, template_name='home.html')


@login_required()
def customer_page(request):
    return render(request, template_name='home.html')


@login_required()
def courier_page(request):
    return render(request, template_name='home.html')


def sign_up(request):
    form = forms.SignUpForm()
    context = {"form": form}
    return render(request, template_name='sign_up.html', context=context)
    