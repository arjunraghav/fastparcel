from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            
            user = form.save(commit = False)
            user.username = email
            user.save()

            # Send a mail

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            return redirect('/')

    context = { "form": form }
    return render(request, template_name='sign_up.html', context=context)
    