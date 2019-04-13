import xlrd
from .models import *
#from django.contrib.auth.models import User,Group
import random
class building_data():
    loc =("/home/singh/Downloads/MOCK_DATA(4).xlsx")
    h=['R','G','Y']
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in building.objects.all():
        for j in panel.objects.all():
            for k in zone.objects.all():
                r = random.randint(0,2)
                c= random.randint(1,99)
                d = device(zone=k,building=i,panel=j,name = "FS{r*r*r}",health=h[r])
                d.save()
