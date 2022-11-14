from django.core.management.base import BaseCommand, CommandError
from database.models import Color, Gobo

import csv

class Command(BaseCommand):
    help = 'Uploads gobo objects from a CSV scraped from manufacturer websites.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        goboCSV = open('LightLine/roscoGobosClean.csv', 'r')  
        for line in goboCSV:
            line =  line.split(',')
            if len(line[0]) == 1:
                pass
            else:
                #check if a gobo with the given name already exists
                if(Gobo.objects.filter(colorName=line[1]).exists()):
                    #gobo exists, so do not add another
                    pass
                else:
                    #gobo does not yet exist, add it
                    try:
                        gobo = Gobo()  
                        gobo.goboCode = line[0]
                        gobo.goboName = line[1]
                        gobo.imageUrl = line[2]
                        gobo.save()
                        self.stdout.write(gobo)
                    except:
                        raise CommandError('Gobo "%s" could not be uploaded' % line[0])


        goboCSV.close()
        self.stdout.write(self.style.SUCCESS('Successfully added Gobos'))
