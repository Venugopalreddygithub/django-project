from django.db import models

# Create your models here.
class Persons(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)

    class Meta:
        #The name of the database for the model
        db_table = "persons"