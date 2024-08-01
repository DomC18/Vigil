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
    return render(request, 'config.html', {'content': content, 'configcontent': configcontent, 'display_curr_config': display_curr_config, 'display_sub_config': display_sub_config, 'link_index': 0})

def subsystemconfigs(request:WSGIRequest):
    currconfigs = get_all_with_username(CurrentConfiguration)
    robotconfigs = get_all_with_username(RobotConfiguration)
    subsystemconfigs = get_all_with_username(SubsystemConfiguration)
    subsystems = get_all_with_username(Subsystem)

    content = currconfigs
    configcontent = subsystemconfigs
    display_curr_config = True if (robotconfigs and subsystemconfigs and not currconfigs) else False
    display_sub_config = True if (subsystems) else False
    return render(request, 'config.html', {'content': content, 'configcontent': configcontent, 'display_curr_config': display_curr_config, 'display_sub_config': display_sub_config, 'link_index': 1})

def subsystems(request:WSGIRequest):
    currconfigs = get_all_with_username(CurrentConfiguration)
    robotconfigs = get_all_with_username(RobotConfiguration)
    subsystemconfigs = get_all_with_username(SubsystemConfiguration)
    subsystems = get_all_with_username(Subsystem)

    content = currconfigs
    configcontent = subsystems
    display_curr_config = True if (robotconfigs and subsystemconfigs and not currconfigs) else False
    display_sub_config = True if (subsystems) else False
    return render(request, 'config.html', {'content': content, 'configcontent': configcontent, 'display_curr_config': display_curr_config, 'display_sub_config': display_sub_config, 'link_index': 2})

def deleterobotconfig(request, robotconfig_id):
    robotconfig = RobotConfiguration.objects.get(pk=robotconfig_id)
    robotconfig.delete()
    return redirect('config')

def deletesubsystemconfig(request, subconfig_id):
    subsystemconfig = SubsystemConfiguration.objects.get(pk=subconfig_id)
    subsystemconfig.delete()
    return redirect('subsystemconfigs')

def deletesubsystem(request, sub_id):
    subsystem = Subsystem.objects.get(pk=sub_id)
    subsystem.delete()
    return redirect('subsystems')

def editrobotconfig(request, robotconfig_id):
    robotconfig = RobotConfiguration.objects.get(pk=robotconfig_id)
    form = RobotConfigForm(request.POST or None, request.FILES, instance=robotconfig)
    if form.is_valid():
        form.save()
        return redirect('robotconfigs')
    return render(request, "updaterobotconfig.html", {'form': form, 'name': gv.current_user, 'instance': robotconfig})

def editsubsystemconfig(request, subconfig_id):
    subconfig = SubsystemConfiguration.objects.get(pk=subconfig_id)
    subsystems = get_all_with_username(Subsystem)
    form = SubsystemConfigForm(request.POST or None, instance=subconfig)
    if form.is_valid():
        form.save()
        return redirect('subsystemconfigs')
    return render(request, "updatesubsystemconfig.html", {'form': form, 'name': gv.current_user, 'instance': subconfig, 'subsystems': subsystems})

def editsubsystem(request, sub_id):
    subsystem = Subsystem.objects.get(pk=sub_id)
    form = SubsystemForm(request.POST or None, request.FILES, instance=subsystem)
    if form.is_valid():
        form.save()
        return redirect('subsystems')
    return render(request, "updatesubsystem.html", {'form': form, 'name': gv.current_user, 'instance': subsystem})

def activaterobotconfig(request, robotconfig_id):
    currconfig = get_all_with_username(CurrentConfiguration)
    if currconfig:
        robotconfig = RobotConfiguration.objects.get(pk=robotconfig_id)
        currconfig[0].RobotConfig = robotconfig
        currconfig[0].save()
    return redirect('robotconfigs')

def activatesubsystemconfig(request, subconfig_id):
    currconfig = get_all_with_username(CurrentConfiguration)
    if currconfig:
        subconfig = SubsystemConfiguration.objects.get(pk=subconfig_id)
        currconfig[0].SubsystemConfig = subconfig
        currconfig[0].save()
    return redirect('subsystemconfigs')

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
        form = RobotConfigForm(request.POST, request.FILES)
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
        form = SubsystemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('config')
    else:
        form = SubsystemForm
        return render(request, 'newsubsystem.html', {'name': gv.current_user})