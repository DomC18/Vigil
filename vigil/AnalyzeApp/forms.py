from django import forms
from .models import AnalyzeConfig

class AnalyzeConfigForm(forms.ModelForm):
    class Meta:
        model = AnalyzeConfig
        fields = [
            "CreatedBy",
            "CurrentConfig",
            "CompName",
            "MatchNumber",
            "AnalyzeFile"
        ]
        widgets = {
            "CurrentConfig": forms.Select(attrs={"class": "form-input"}),
            "CompName": forms.TextInput(attrs={"class": "form-input"}),
            "MatchNumber": forms.NumberInput(attrs={"class": "form-input"}),
            "AnalyzeFile": forms.FileInput(attrs={"class": "form-input"})
        }