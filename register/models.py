from django.db import models

# Create your models here.
class placeholder(models.Model):
    user = models.CharField(max_length=100,default ='Username' )
    userlast= models.CharField(max_length=100 ,default ='lastname' )
    username= models.CharField(max_length=100 ,default ='username' )
    phno = models.CharField(max_length=100, default ='PhoneNumber')
    mail = models.CharField(max_length=100 , default ='Mail_id')
    pas  = models.CharField(max_length=100,default ='Password') 
    cnfpass = models.CharField(max_length=100,default='Confirm Password')
    img = models.ImageField(upload_to='pics', default ='C:/Users/vansh/Envs/test/project/login/static/images/image-1.png')
    img2 = models.ImageField(upload_to='pics1' , default ='C:/Users/vansh/Envs/test/project/login/static/images/image-2.png')

