from .methods import get_all_with_username, last_with_username
from django.core.handlers.wsgi import WSGIRequest
from ConfigApp.models import CurrentConfiguration
from django.shortcuts import render, redirect
from .graphs import Graph, get_numeric_columns
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
        currconfig = get_all_with_username(CurrentConfiguration)
        return render(request, 'analyzeform.html', {'form': form, 'name': gv.current_user, 'currconfig': currconfig[0]})

def analyzematch(request:WSGIRequest):
    path = os.path.join(settings.BASE_DIR, ("media" + rf"{gv.current_data}"))
    columns = get_numeric_columns(path)
    graphs = [Graph(path, col_name) for col_name in columns]
    graphs = [graph.to_html() for graph in graphs]
    return render(request, 'analyzematch.html', {'name': gv.current_user, 'graphs': graphs})