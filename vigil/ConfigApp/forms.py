from django import forms
from .models import CurrentConfiguration, RobotConfiguration, SubsystemConfiguration, Subsystem

class CurrentConfigForm(forms.ModelForm):
    class Meta:
        model = CurrentConfiguration
        fields = [
            "CreatedBy",
            "SubsystemConfig",
            "RobotConfig"
        ]
        widgets = {
            "SubsystemConfig": forms.RadioSelect(attrs={"class": "form-radio"}, choices=[(s.id) for s in SubsystemConfiguration.objects.all()]),
            "RobotConfig": forms.RadioSelect(attrs={"class": "form-radio"}, choices=[(s.id) for s in RobotConfiguration.objects.all()])
        }

class RobotConfigForm(forms.ModelForm):
    class Meta:
        model = RobotConfiguration
        fields = [
            "CreatedBy",
            "RobotName",
            "RobotImage",
            "FRCYear", 
            "TeamNumber",
            "DriveTrainType"
        ]
        widgets = {
            "RobotName": forms.TextInput(attrs={"class": "form-input"}),
            "RobotImage": forms.FileInput(attrs={"class": "form-input"}),
            "FRCYear": forms.NumberInput(attrs={"class": "form-input"}),
            "TeamNumber": forms.NumberInput(attrs={"class": "form-input"}),
            "DriveTrainType": forms.TextInput(attrs={"class": "form-input"}),
        }

class SubsystemConfigForm(forms.ModelForm):
    class Meta:
        model = SubsystemConfiguration
        fields = [
            "CreatedBy",
            "SubConfigName",
            "Subsystems"
        ]
        widgets = {
            "SubConfigName": forms.TextInput(attrs={"class": "form-input"}),
            "Subsystems": forms.CheckboxSelectMultiple(attrs={"class": "form-checkbox"}, choices=[(s.id) for s in Subsystem.objects.all()])
        }

class SubsystemForm(forms.ModelForm):
    class Meta:
        model = Subsystem
        fields = [
            "CreatedBy",
            "SubsystemName",
            "SubsystemImage"
        ]
        widgets = {
            "SubsystemName": forms.TextInput(attrs={"class": "form-input"}),
            "SubsystemImage": forms.FileInput(attrs={"class": "form-input"})
        }