from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
import csv
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404 

from .models import Site
from .forms import SiteForm

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def site_list(request):
    sites = Site.objects.filter(user=request.user)
    return render(request, 'site_list.html', {'sites': sites})

@login_required
def add(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            return redirect('site_list')
    else:
        form = SiteForm()
    return render(request, 'add.html', {'form': form})

@login_required
def edit(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_list')
    else:
        form = SiteForm(instance=site)
    return render(request, 'edit.html', {'form': form, 'site': site})  # Passer 'site' dans le contexte

@login_required
def delete(request, pk):
    site = Site.objects.get(pk=pk)
    site.delete()
    return redirect('site_list')

@login_required
def export_sites_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sites.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'URL', 'Identifier', 'Password'])
    sites = Site.objects.filter(user=request.user)
    for site in sites:
        writer.writerow([site.name, site.url, site.identifier, site.password])
    return response

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})