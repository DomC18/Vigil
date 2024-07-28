from django import forms
from .models import CurrentConfiguration, RobotConfiguration, SubsystemConfiguration, Subsystem

# class CurrentConfigForm(forms.ModelForm):
#     class Meta:
#         model = CurrentConfiguration
#         fields = [
#             "Subsystem Config",
#             "Robot Config"
#         ]
#         widgets = {
#             "Subsystem Config": forms.CheckboxSelectMultiple(choices=[(s.id) for s in SubsystemConfiguration.objects.all()]),
#             "Robot Config": forms.CheckboxSelectMultiple(choices=[(s.id) for s in RobotConfiguration.objects.all()])
#         }
#         labels = {
#             "Subsystem Config": "Select Subsystem Configurations",
#             "Robot Config": "Select Robot Configurations"
#         }

class RobotConfigForm(forms.ModelForm):
    class Meta:
        model = RobotConfiguration
        fields = [
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
        labels = {
            "Robot Name": "Robot Name",
            "Robot Image": "Upload Robot Image",
            "FRC Year": "FRC Year",
            "Team Number": "Team Number",
            "DriveTrain Type": "Drivetrain Type"
        }

# class SubsystemConfigForm(forms.ModelForm):
#     class Meta:
#         model = SubsystemConfiguration
#         fields = [
#             "Subsystem Configuration Name"
#             "Subsystems"
#         ]
#         widgets = {
#             "Subsystem Configuration Name": forms.TextInput(attrs={"class": "form-input"}),
#             "Subsystems": forms.CheckboxSelectMultiple(choices=[(s.id) for s in Subsystem.objects.all()])
#         }
#         labels = {
#             "Subsystem Configuration Name": "Subsystem Config Name",
#             "Subsystems": "Select Subsystems"
#         }

class SubsystemForm(forms.ModelForm):
    class Meta:
        model = Subsystem
        fields = [
            "Subsystem Name",
            "Subsystem Image"
        ]
        widgets = {
            "Subsystem Name": forms.TextInput(attrs={"class": "form-input"}),
            "Subsystem Image": forms.FileInput(attrs={"class": "form-input"})
        }
        labels = {
            "Subsystem Name": "Subsystem Name",
            "Subsystem Image": "Upload Subsystem Image"
        }