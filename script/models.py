from django.db import models

from projects.models import Project

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
