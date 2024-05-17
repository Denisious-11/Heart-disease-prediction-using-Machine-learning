from django.db import models



class Patients_table(models.Model):
    name=models.CharField(max_length=250)
    age=models.CharField(max_length=250)
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=300)
    username=models.CharField(max_length=300,unique=True)
    password=models.CharField(max_length=300)
    
class Doctor_table(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=300)
    place=models.CharField(max_length=250)
    username=models.CharField(max_length=300,unique=True)
    password=models.CharField(max_length=300)

class Chat_table(models.Model):
    From=models.CharField(max_length=250)
    To=models.CharField(max_length=300)
    chat=models.CharField(max_length=300)
    

class Files(models.Model):
    f_id=models.IntegerField(primary_key=True)
    filename=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    time=models.CharField(max_length=255)
   