from django.db import models

from projects.models import Project

#Regex for csv parsing
import re

class Breakout(models.Model):
    id = models.AutoField(primary_key=True)
    circuitLabel = models.CharField(max_length = 32, unique=True)
    service = models.IntegerField()

class Circuit(models.Model):
    id = models.AutoField(primary_key=True)
    circuitLabel = models.CharField(max_length = 32, unique=True)
    service = models.IntegerField()
    breakout = models.ForeignKey(Breakout, on_delete=models.CASCADE)


class CableType(models.Model):
    id = models.AutoField(primary_key=True)
    cableTypeName = models.CharField(max_length = 32, unique=True)
    weightPerFoot = models.IntegerField()
    ampRating = models.IntegerField()
    power = models.BooleanField(default=False)
    data = models.BooleanField(default=False)

class Cable(models.Model):
    id = models.AutoField(primary_key=True)
    cableLabel = models.CharField(max_length = 32, unique=True)
    cableType = models.CharField(max_length = 16, unique=True)
    cableLength = models.IntegerField()
    weight = models.IntegerField()


class Gobo(models.Model):
    id = models.AutoField(primary_key=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    goboName = models.CharField(max_length = 64)
    goboCode = models.CharField(max_length = 32, unique=True)
    imageUrl = models.CharField(max_length = 128)

    def __str__(self):
        return self.goboCode


#Defines a Color filter model
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    
    #Prose name, Numerical code, and hex color code for displaying swatch
    colorName = models.CharField(max_length = 32)
    colorCode = models.CharField(max_length = 16, unique=True)
    colorHex = models.CharField(max_length = 32, default="0xFFFFFFFF")

    def __str__(self):
        return self.colorCode

    # #Get the Color instance matching the provided name
    # def getColor(self, name):
    #     try:
    #         return Color.objects.get(colorName = name)
    #     except:
    #         return None


class Accessory(models.Model):
    id = models.AutoField(primary_key=True)
    accessoryName = models.CharField(max_length = 32, unique=True)
    weight = models.IntegerField()

class FocusChart(models.Model):
    id = models.AutoField(primary_key=True)
    chartLabel = models.CharField(max_length = 32, unique=False)


class FocusNote(models.Model):
    id = models.AutoField(primary_key=True)
    noteLabel = models.CharField(max_length = 32, unique=False)

class WorkNote(models.Model):
    id = models.AutoField(primary_key=True)
    noteLabel = models.CharField(max_length = 32, unique=False)


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    positionName = models.CharField(max_length = 32, unique=True)

    def __str__(self):
        return self.positionName


class InstrumentType(models.Model):
    id = models.AutoField(primary_key=True)
    typeName = models.CharField(max_length = 64)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    load = models.FloatField(blank=True, null=True)
    beamAngle = models.IntegerField(blank=True, null=True)
    fieldAngle = models.IntegerField(blank=True, null=True)
    zoomAngleMin = models.IntegerField(blank=True, null=True)
    zoomAngleMax = models.IntegerField(blank=True, null=True)
    zoomAble = models.BooleanField(default=False, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.typeName

#Defines a Lighting Instrument
class Instrument(models.Model):
    id = models.AutoField(primary_key=True)
    #Project that this instrument is associated with - this instrument instance will only be associated with one project
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    #Instrument Type - Instrument types are local to projects, but many instruments can share type
    instrumentType = models.ForeignKey(InstrumentType, on_delete=models.CASCADE, blank=True, null=True)
    #Position - Positions are local to projects, but many instruments can share position
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    unitNumber = models.IntegerField(blank=True, null=True)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ManyToManyField(Color, related_name="colors", blank=True)
    gobo = models.ForeignKey(Gobo, on_delete=models.CASCADE, blank=True, null=True)
    goboSize = models.CharField(max_length = 8, unique=False, blank=True, null=True)
    purpose = models.CharField(max_length = 128, blank=True, null=True)
    #Dimmer - currentyl a CharField to deal with doubled dimmers
    #TODO - abstract Dimmer to its own class
    dimmer = models.CharField(max_length = 32, blank=True, null=True)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE, blank=True, null=True)
    breakout = models.ForeignKey(Breakout, on_delete=models.CASCADE, blank=True, null=True)
    dimmerPhase = models.CharField(max_length = 8, unique=False, blank=True, null=True)
    address = models.IntegerField(blank=True, null=True)
    universe = models.IntegerField(blank=True, null=True)
    channel = models.IntegerField(blank=True, null=True)
    focusChart = models.ForeignKey(FocusChart, on_delete=models.CASCADE, blank=True, null=True)
    cable = models.ForeignKey(Cable, on_delete=models.CASCADE, blank=True, null=True)
    focusNote = models.ForeignKey(FocusNote, on_delete=models.CASCADE, blank=True, null=True)
    workNote = models.ForeignKey(WorkNote, on_delete=models.CASCADE, blank=True, null=True)

    #Return all colors associated with this Instrument
    def getColors(self):
        return self.color.all()

    def __str__(self):
        return str(self.instrumentType) + " CHANNEL " + str(self.channel)

    #Add Instrument instanced from a csv file exported from LightWright 6
    def addInstrumentsFromCSV(csv, activeProject):
        #split csv into lines
        csv = csv.splitlines()
        for line in csv:
            #decode to bytes-like object
            line_decoded = line.decode()
            #split into col elements by comma
            cols = line_decoded.split(',')

            #check fro empty line or header
            if len(cols[0]) == 1 or cols[0] == "Purpose":
                pass
            #else, parse data and create instrument object
            else: 
                instrument = Instrument()
                #PROJECT
                instrument.project = activeProject
                #PURPOSE
                instrument.purpose = cols[0]
                #CHANNEL
                if cols[1] != '':
                    chan = cols[1]
                    chan = re.search('\(([^)]+)', chan).group(1)
                    instrument.channel = chan
                #DIMMER
                if cols[2] != '':
                    instrument.dimmer = cols[2]
                else:
                    pass
                #ADDRESS - need to parse out universe
                # if line[3] != '':
                #     instrument.address = line [3]
                # else:
                #     pass
                #POSITION
                try:
                    instrument.position = Position.objects.get(positionName = cols[4])
                except:
                    newPosition = Position()
                    newPosition.positionName = cols[4]
                    newPosition.save()
                    instrument.position = newPosition

                #UNIT #
                if cols[4] != '':
                    instrument.unitNumber = cols[5]
                else:
                    pass
                #INSTRUMENT TYPE
                #if instrument type exists, use existing type
                try:
                    instrument.instrumentType =  InstrumentType.objects.get(typeName = cols[6])
                #if no type exists, create a new one
                except:
                    newType = InstrumentType()
                    newType.typeName = cols[6]

                    #extract float from wattage by removing "w"s
                    loadString = cols[7]
                    if loadString != '':
                        #handle loads written in kW format
                        if "kW" in loadString:
                            loadFloat = float(re.sub("kW", " ", loadString)) * 1000
                            print(loadFloat)
                        #if not in kW format, remove w and convert to float
                        else:
                            loadCleaned = re.sub("w", " ", loadString)
                            loadFloat = float(loadCleaned)
                        #set load of new type to parsed wattage
                        newType.load = loadFloat
                    else:
                        pass
                    newType.project = activeProject
                    newType.save()
                    instrument.instrumentType = newType

                #ACCESSORY
                # if Accessory.objects.get(accessoryName = line[8]):
                #     instrument.position = Position.objects.get(accessoryName = line[8])
                # else:
                #     newAccessory = Accessory()
                #     newAccessory.accessoryName = line[8]
                #     instrument.accessory = newAccessory
                
                #COLOR
                colorString = cols[9]
                
                colorSplit = re.sub('\s+', '+', colorString).split("+")

                #SAVE TO ALLOW MANY TO MANY
                instrument.save()

                for name in colorSplit:
                    try:
                        instrument.color.add(Color.objects.get(colorCode = name))
                        print("FOUND " + name)

                    except:
                        print("COLOR NOT FOUND " + name)
                        pass


                #GOBO

                goboString = cols[10]
                
                #SPLIT THE STRING, WE SHOULD ONLY LOOK AT THE FIRST SET OF CHARACTERS BEFORE A SPACE, IF A SPACE EXISTS
                goboSplit = goboString.split(" ")


                for name in goboSplit:
                    try:
                        instrument.gobo = (Gobo.objects.get(goboCode = name))
                        print("GOBO FOUND " + name)

                    except:
                        print("GOBO NOT FOUND " + name)
                        pass


                #SAVE INSTRUMENT
                instrument.save()  
