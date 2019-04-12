from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20,unique=True)


    def __str__(self):
        return f"{self.id} {self.username}"

class zone(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone_no = models.IntegerField()
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.name}"

class building(models.Model):
    zone = models.ForeignKey(to=zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return f"{self.id} {self.name}"

class panel(models.Model):
    building = models.ForeignKey(to=building, on_delete=models.CASCADE)
    location = models.TextField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id} {self.name}"

class device(models.Model):
    zone = models.ForeignKey(to=zone, on_delete=models.CASCADE)
    building = models.ForeignKey(to=building,on_delete=models.CASCADE)
    panel = models.ForeignKey(to=panel, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date_time_created = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateTimeField(auto_now=True)
    health = models.CharField(max_length=1) #Y G R

    def __str__(self):
        return f"{self.id} {self.health} {self.zone.id} {self.building.id} {self.panel.id} "
