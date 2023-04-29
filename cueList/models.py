from django.db import models

from projects.models import Project


class CueList(models.Model):
    id = models.AutoField(primary_key=True)
    listName = models.CharField(max_length = 64)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    cueListNumber = models.FloatField(default=1)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.listName

    def getLastCue(self):
        cuesInList = Cue.objects.order_by('eosCueNumber').filter(cueList=self)
        try:
            lastCue= cuesInList[len(cuesInList) - 1]
            return lastCue.id
        except:
            return 0


class CueManager(models.Manager):
    def createNext(self, lastCueNum, cueList):

        increment = 2

        cue = self.create(eosCueNumber= lastCueNum + increment, cueList=cueList)

        return cue


class Cue(models.Model):
    id = models.AutoField(primary_key=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    cueLabel = models.CharField(max_length = 100, default="", blank=True)
    pageNumber = models.IntegerField(default=1)
    eosCueNumber = models.FloatField(default=1)
    cueTime = models.FloatField(default=5)
    cueDescription = models.CharField(max_length = 100, default="", blank=True)
    cueList = models.ForeignKey(CueList, on_delete=models.CASCADE, default=1)

    # block = models.BooleanField(default=False)

    objects = CueManager()


    def __str__(self):
        return self.cueLabel


    #Return array of Actions that have this spot cue as their cue field
    def getActions(self):
        try:
            return Action.objects.filter(cue=self)
        except:
            None

    #Return Header for cue if exists
    def getHeader(self):
        try:
            return Header.objects.get(cue=self)
        except:
            return None
    #Add Cue instanced from a csv file exported from ETC Eos
    def addCuesFromCSV(csv, activeProject):
        #split csv into lines
        csv = csv.splitlines()
        #create new Cue List
        cueListLine = csv[2].decode().split(',')
        cueList = CueList()
        cueList.listName = cueListLine[6]
        cueList.project = activeProject
        cueList.cueListNumber = cueListLine[3]
        cueList.active = True
        cueList.save()

        for line in csv:
            #decode to bytes-like object
            line_decoded = line.decode()
            #split into col elements by comma
            cols = line_decoded.split(',')
            
            #bypass last line
            if cols[0] != "END_TARGETS":
                #check for headers or part cues
                if cols[0] == "START_TARGETS" or cols[0] == "TARGET_TYPE" or cols[0] == "15" or cols[5] != "":
                    pass
                #else, parse data and create instrument object
                else: 
                    cue = Cue()
                    #LABEL
                    cue.cueLabel = cols[6]
                    #CUE NUMBER
                    cue.eosCueNumber = float(cols[3])
                    #CUE TIME
                    if cols[7] != '':
                        cue.cueTime = float(cols[7])
                    else:
                        cue.cueTime = 4.9
                    #CUE LIST
                    cue.cueList = cueList

                    #SAVE INSTRUMENT
                    cue.save()  



class Header(models.Model):
    id = models.AutoField(primary_key=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    cue = models.ForeignKey(Cue, default=1, on_delete=models.CASCADE)
    headerTitle = models.CharField(max_length = 100, default="", blank=True)
    cueList = models.ForeignKey(CueList, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.headerTitle



