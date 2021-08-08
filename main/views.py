from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def commands(request):
    return render(request, 'main/commands.html')

def add(request):
    return redirect('https://discord.com/oauth2/authorize?client_id=873296088025686016&permissions=0&scope=bot')