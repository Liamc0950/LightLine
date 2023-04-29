from django.db import models

from projects.models import Project
from cueList.models import Cue

class Script(models.Model):
    id = models.AutoField(primary_key=True)
    scriptName = models.CharField(max_length = 128)
    pdf = models.FileField(upload_to='pdfs/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['scriptName']
     
    def __str__(self):
        return self.scriptName

    def activate(self):
        scripts = Script.objects.filter(project=self.project, active=True)
        for script in scripts:
            script.active = False
        self.active = True
        self.save()

class Annotation(models.Model):
    #reference fields
    id = models.AutoField(primary_key=True)
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    page = models.IntegerField(default=1)

    #position on canvas
    xPos = models.FloatField(default=0)
    yPos = models.FloatField(default=0)

    class Meta:
        abstract = True

class CueAnnotation(Annotation):
    cue = models.ForeignKey(Cue, on_delete=models.CASCADE)
    note = models.CharField(max_length=256, blank=True)