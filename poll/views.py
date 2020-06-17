from django.shortcuts import render,redirect
from .models import applicant
from django.db.models import F

def redirect_view(request):
    response = redirect('/Dgsec/')
    return response

def Dgsec(request):
    if request.method == 'POST':
         selected_candidate = request.POST['poll']
         candidate = applicant.objects.get(name=selected_candidate)
         candidate.count += 1
         candidate.save()
    context = {
        'applicant':applicant.objects.filter(post='Dgsec')
          }
    return render(request, 'home.html' , context)

def Gsec(request):
    if request.method == 'POST':
         selected_candidate = request.POST['poll']
         candidate = applicant.objects.get(name=selected_candidate)
         candidate.count += 1
         candidate.save()
    context = {
        'applicant':applicant.objects.filter(post='Gsec')
          }
    return render(request, 'home.html' , context)

def pgrep(request):
    if request.method == 'POST':
         selected_candidate = request.POST['poll']
         candidate = applicant.objects.get(name=selected_candidate)
         candidate.count += 1
         candidate.save()
    context = {
        'applicant':applicant.objects.filter(post='pgrep')
          }
    return render(request, 'home.html' , context)
