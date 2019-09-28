from django.db import models

# Create your models here.
class Contact(models.Model):
    c_id =models.AutoField(primary_key=True)
    nm =models.CharField(max_length=100)
    em =models.CharField(max_length=100)
    no =models.CharField(max_length=12)
    msg =models.CharField(max_length=500)

class Blog(models.Model):
    b_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    img=models.FileField(upload_to="blog" ,default="")
