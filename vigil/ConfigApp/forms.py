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
            "Robot Name",
            "Robot Image",
            "FRC Year", 
            "Team Number",
            "DriveTrain Type"
        ]
        widgets = {
            "Robot Name": forms.TextInput(attrs={"class": "form-input"}),
            "Robot Image": forms.FileInput(attrs={"class": "form-input"}),
            "FRC Year": forms.NumberInput(attrs={"class": "form-input"}),
            "Team Number": forms.NumberInput(attrs={"class": "form-input"}),
            "DriveTrain Type": forms.TextInput(attrs={"class": "form-input"}),
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
            "Subsystem Name",
            "Subsystem Image"
        ]
        widgets = {
            "Subsystem Name": forms.TextInput(attrs={"class": "form-input"}),
            "Subsystem Image": forms.FileInput(attrs={"class": "form-input"})
        }