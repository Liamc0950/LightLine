from django.db import models

from accounts.models import Profile

#Project - Defines the 
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    lastUpdate = models.DateTimeField(auto_now=True)

    #Name of show
    showName = models.CharField(max_length = 128)
    showNameShort = models.CharField(max_length = 8, default="")

    #Show Info
    venue = models.CharField(max_length = 128)
    

    #Profile of the project creator
    #This Profile automatically be assigned as the Lighting Designer by default
    projectCreator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    #If true, database, cueList, Followspot and notes views will display data from this project
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.showName

    def isActive(self):
        return self.active
    
    # Activate project and deactive all others
    def activate(self, profile):
        self.deactivateOthers(profile)
        self.active = True
        self.save()
        print(self.showName, " ACTIVATED ", self.active)
    
    def deactivateOthers(self, profile):
        userProjects = Project.objects.filter(projectCreator= profile, active=True)
        for project in userProjects:
            print("DEACTIVATE: ", project)
            project.active = False
            project.save()
