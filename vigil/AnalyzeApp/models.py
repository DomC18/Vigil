from django.db import models
from ConfigApp.models import CurrentConfiguration

class AnalyzeConfig(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    current_configuration = models.ForeignKey(name="CurrentConfig", to=CurrentConfiguration, blank=True, null=True, on_delete=models.CASCADE)
    comp_name = models.CharField(name="CompName", max_length=100, blank=True)
    match_number = models.IntegerField(name="MatchNumber", default=0, blank=True)
    analyze_file = models.FileField(name="AnalyzeFile", blank=True, null=True, upload_to="datafiles/")

    def __str__(self):
        return f"{self.CompName} match {self.MatchNumber}"