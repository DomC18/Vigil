from .models import SubsystemConfiguration, RobotConfiguration, Subsystem, CurrentConfiguration
from .forms import RobotConfigForm, SubsystemConfigForm, SubsystemForm, CurrentConfigForm
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from .methods import get_all_with_username
import globalvariables as gv

def config(request:WSGIRequest):
    currconfigs = get_all_with_username(CurrentConfiguration)
    robotconfigs = get_all_with_username(RobotConfiguration)
    subsystemconfigs = get_all_with_username(SubsystemConfiguration)
    subsystems = get_all_with_username(Subsystem)

    content = currconfigs
    configcontent = robotconfigs
    display_curr_config = True if (robotconfigs and subsystemconfigs and not currconfigs) else False
    display_sub_config = True if (subsystems) else False
    return render(request, 'config.html', {'content': content, 'configcontent': configcontent, 'display_curr_config': display_curr_config, 'display_sub_config': display_sub_config})

def subsystemconfigs(request:WSGIRequest):
    currconfigs = get_all_with_username(CurrentConfiguration)
    robotconfigs = get_all_with_username(RobotConfiguration)
    subsystemconfigs = get_all_with_username(SubsystemConfiguration)
    subsystems = get_all_with_username(Subsystem)

    content = currconfigs
    configcontent = subsystemconfigs
    display_curr_config = True if (robotconfigs and subsystemconfigs and not currconfigs) else False
    display_sub_config = True if (subsystems) else False
    return render(request, 'config.html', {'content': content, 'configcontent': configcontent, 'display_curr_config': display_curr_config, 'display_sub_config': display_sub_config})

def subsystems(request:WSGIRequest):
    currconfigs = get_all_with_username(CurrentConfiguration)
    robotconfigs = get_all_with_username(RobotConfiguration)
    subsystemconfigs = get_all_with_username(SubsystemConfiguration)
    subsystems = get_all_with_username(Subsystem)

    content = currconfigs
    configcontent = subsystems
    display_curr_config = True if (robotconfigs and subsystemconfigs and not currconfigs) else False
    display_sub_config = True if (subsystems) else False
    return render(request, 'config.html', {'content': content, 'configcontent': configcontent, 'display_curr_config': display_curr_config, 'display_sub_config': display_sub_config})

def newcurrentconfig(request:WSGIRequest):
    if request.method == "POST":
        form = CurrentConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = CurrentConfigForm
        subsystemconfigs = get_all_with_username(SubsystemConfiguration)
        robotconfigs = get_all_with_username(RobotConfiguration)
        return render(request, 'newcurrentconfig.html', {'form': form, 'name': gv.current_user, "subsystemconfigs": subsystemconfigs, "robotconfigs": robotconfigs})

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
        subsystems = get_all_with_username(Subsystem)
        return render(request, 'newsubsystemconfig.html', {"form": form, 'name': gv.current_user, "subsystems": subsystems})

def newsubsystem(request:WSGIRequest):
    if request.method == "POST":
        form = SubsystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = SubsystemForm
        return render(request, 'newsubsystem.html', {'name': gv.current_user})