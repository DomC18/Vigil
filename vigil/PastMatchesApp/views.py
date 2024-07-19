from django.shortcuts import render

# Create your views here.
def pastmatches(request):
    return render(request, 'pastmatches.html')