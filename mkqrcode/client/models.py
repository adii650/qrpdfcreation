from django.db import models

# Create your models here.
class Client(models.Model):
    clientname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='client_data')
    status=models.BooleanField(default=False)
class clientinfo(models.Model):
    contactno=models.CharField(max_length=10)
    adhar=models.CharField(max_length=12)
    adress=models.CharField(max_length=50)
    district=models.CharField(max_length=15)
    place=models.CharField(max_length=15)
    qualification=models.CharField(max_length=15)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
class clientdocument(models.Model):
    pdfdata=models.FileField(upload_to='DOCUMENTS',null=True,blank=True)
    qrdata=models.ImageField(upload_to='qrcode',null=True,blank=True)
    client=models.ForeignKey(clientinfo,on_delete=models.CASCADE)