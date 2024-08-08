from .methods import get_all_with_username, last_with_username
from django.core.handlers.wsgi import WSGIRequest
from ConfigApp.models import CurrentConfiguration
from django.shortcuts import render, redirect
from .graphs import LineGraph, get_numeric_columns, group_graphs
from .forms import AnalyzeConfigForm
from .models import AnalyzeConfig
import vigil.settings as settings
import globalvariables as gv
import os

def analyze(request:WSGIRequest):
    if request.method == "POST":
        form = AnalyzeConfigForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            gv.current_data = last_with_username(AnalyzeConfig).AnalyzeFile.url
            return redirect('analyzematch')
    else:
        form = AnalyzeConfigForm
        try: currconfig = get_all_with_username(CurrentConfiguration)[0] 
        except: currconfig = None
        return render(request, 'analyzeform.html', {'form': form, 'name': gv.current_user, 'currconfig': currconfig})

def analyzematch(request:WSGIRequest):
    path = os.path.join(settings.BASE_DIR, ("media" + rf"{gv.current_data}"))
    columns = get_numeric_columns(path)
    graphs = [LineGraph(path, col_name).to_html() for col_name in columns]

    currconfig = get_all_with_username(CurrentConfiguration)[0]
    grouping = group_graphs(path, currconfig)

    return render(request, 'analyzematch.html', {'name': gv.current_user, 'graphs': graphs, 'grouping': grouping})

def pastmatches(request:WSGIRequest):
    matchcontent = get_all_with_username(AnalyzeConfig)
    return render(request, 'pastmatches.html', {'matchcontent': matchcontent})

def deletematch(request, match_id):
    match = AnalyzeConfig.objects.get(pk=match_id)
    match.delete()
    return redirect('pastmatches')

def editmatch(request:WSGIRequest, match_id):
    match = AnalyzeConfig.objects.get(pk=match_id)
    currconfig = get_all_with_username(CurrentConfiguration)[0]
    form = AnalyzeConfigForm(request.POST or None, request.FILES, instance=match)
    if form.is_valid():
        form.save()
        return redirect('pastmatches')
    return render(request, 'editmatch.html', {'form': form, 'name': gv.current_user, 'instance': match, 'currconfig': currconfig})

def openmatch(request:WSGIRequest, match_id):
    match = AnalyzeConfig.objects.get(pk=match_id)
    gv.current_data = match.AnalyzeFile.url
    return redirect('analyzematch')