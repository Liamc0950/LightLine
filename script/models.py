from django.db import models

from projects.models import Project

class Script(models.Model):
    id = models.AutoField(primary_key=True)
    scriptName = models.CharField(max_length = 128, unique=True)
    pdf = models.FileField(upload_to='pdfs/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['scriptName']
     
    def __str__(self):
        return f"{self.scriptName}"