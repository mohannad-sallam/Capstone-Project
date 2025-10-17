from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Parts


@login_required
def home(request):
    parts = Parts.objects.all()
    return render(request, 'home.html', {'parts': parts})



@login_required
def part_detail(request, pk):
    part = get_object_or_404(Parts, pk=pk) # in here i used get_object_or_404 instead of object.get() because it returnes 404 page not founf if there was no part found instead of 500 server error
    return render(request, 'part_detail.html', {'part': part})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
