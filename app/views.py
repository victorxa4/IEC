from django.shortcuts import render, redirect

def home_view(request):
    print('test')
    return render(request, 'home.html', context={})