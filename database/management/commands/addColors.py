from django.core.management.base import BaseCommand, CommandError
from database.models import Color, Gobo

import csv

class Command(BaseCommand):
    help = 'Uploads Color objects from a CSV scraped from manufacturer websites.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        roscoCSV = open('LightLine/roscolux.csv', 'r')  
        for line in roscoCSV:
            line =  line.split(',')
            if len(line[0]) == 1:
                pass
            else:
                #check if a color with the given name already exists
                if(Color.objects.filter(colorName=line[1]).exists()):
                    #color exists, so do not add another
                    pass
                else:
                    #color does not yet exist, add it
                    try:
                        color = Color()  
                        color.colorName = line[1]
                        color.colorCode = line[0]  
                        color.colorHex = line[2]
                        color.save()
                        print(color)
                    except:
                        raise CommandError('Color "%s" could not be uploaded' % line[0])

        roscoCSV.close()
        print(self.style.SUCCESS('Successfully added Rosco Colors'))


        leeCSV = open('LightLine/lee.csv', 'r')  
        for line in leeCSV:
            line =  line.split(',')
            if len(line[0]) == 1:
                pass
            else:
                #check if a color with the given name already exists
                if(Color.objects.filter(colorName=line[1]).exists()):
                    #color exists, so do not add another
                    pass
                else:
                    #color does not yet exist, add it
                    try:
                        color = Color()  
                        color.colorName = line[1]
                        color.colorCode = line[0]  
                        color.colorHex = line[2]
                        color.save()
                        print(color)
                    except:
                        raise CommandError('Color "%s" could not be uploaded' % line[0])


        leeCSV.close() 
        print(self.style.SUCCESS('Successfully added Lee Colors'))
