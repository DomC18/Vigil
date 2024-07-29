from django.shortcuts import render, redirect
from .forms import RobotConfigForm, SubsystemConfigForm, SubsystemForm

# Create your views here.
def config(request):
    return render(request, 'config.html')

# def selectcurrentconfig(request):
#     return render(request, 'selectcurrentconfig.html')

def newrobotconfig(request):
    if request.method == "POST":
        form = RobotConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = RobotConfigForm
        return render(request, 'newrobotconfig.html')

def newsubsystemconfig(request):
    if request.method == "POST":
        form = SubsystemConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = SubsystemConfigForm
        return render(request, 'newsubsystemconfig.html', {"form": form})

def newsubsystem(request):
    if request.method == "POST":
        form = SubsystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = SubsystemForm
        return render(request, 'newsubsystem.html')