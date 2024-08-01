from django.core.handlers.wsgi import WSGIRequest
from ConfigApp.models import CurrentConfiguration
from django.shortcuts import render, redirect
from .methods import get_all_with_username
from .forms import AnalyzeConfigForm
from .models import AnalyzeConfig
import globalvariables as gv

# Create your views here.
def analyze(request:WSGIRequest):
    if request.method == "POST":
        form = AnalyzeConfigForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            gv.current_data = get_all_with_username(AnalyzeConfig)[0].AnalyzeFile.url
            return redirect('analyzematch')
    else:
        form = AnalyzeConfigForm
        currconfig = get_all_with_username(CurrentConfiguration)
        return render(request, 'analyzeform.html', {'form': form, 'name': gv.current_user, 'currconfig': currconfig[0]})

def analyzematch(request:WSGIRequest):
    return render(request, 'analyzematch.html', {'name': gv.current_user, 'currentdata': gv.current_data})