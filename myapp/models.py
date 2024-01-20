from django.db import models

# Create your models here.
class usersingup(models.Model):
      created=models.DateField(auto_now_add=True)
      firstname=models.CharField(max_length=10)
      lastname=models.CharField(max_length=10)
      username=models.CharField(max_length=20)
      password=models.CharField(max_length=10)
      state=models.CharField(max_length=10)
      city=models.CharField(max_length=10)
      number=models.BigIntegerField()


class mynotes(models.Model):
       created=models.DateField(auto_now_add=True)
       query=models.CharField(max_length=10)
      # myfile=models.FileField(upload_to='media')
       myfile=models.FileField(upload_to='Media')
       type_query=models.CharField(max_length=10)
       comment=models.TextField()


class feedback(models.Model):
       created=models.DateField(auto_now_add=True)
       name=models.CharField(max_length=20)
       email=models.EmailField()
       sub=models.CharField(max_length=20)
       msg=models.TextField()