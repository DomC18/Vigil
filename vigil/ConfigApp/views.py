from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .forms import RobotConfigForm, SubsystemConfigForm, SubsystemForm, CurrentConfigForm
import globalvariables as gv

# Create your views here.
def config(request:WSGIRequest):
    return render(request, 'config.html')

def newcurrentconfig(request:WSGIRequest):
    if request.method == "POST":
        form = CurrentConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = CurrentConfigForm
        return render(request, 'newcurrentconfig.html', {'form': form, 'name': gv.current_user})

def newrobotconfig(request:WSGIRequest):
    if request.method == "POST":
        form = RobotConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = RobotConfigForm
        return render(request, 'newrobotconfig.html', {'name': gv.current_user})

def newsubsystemconfig(request:WSGIRequest):
    if request.method == "POST":
        form = SubsystemConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = SubsystemConfigForm
        return render(request, 'newsubsystemconfig.html', {"form": form, 'name': gv.current_user})

def newsubsystem(request:WSGIRequest):
    if request.method == "POST":
        form = SubsystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = SubsystemForm
        return render(request, 'newsubsystem.html', {'name': gv.current_user})