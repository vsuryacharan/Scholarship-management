from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser,User


class CustomUser(AbstractUser):
    pass




class Scholarship(models.Model):
    
    scheme_name = models.CharField(max_length=255,null=True,blank=True)
    Scheme_closing_date= models.CharField(max_length=255,null=True,blank=True)
    defective_verification= models.CharField(max_length=255,null=True,blank=True)
    institute_verification = models.CharField(max_length=255,null=True,blank=True)
    MNO_verification = models.CharField(max_length=255,null=True,blank=True)
    guidelines = models.CharField(max_length=255,null=True,blank=True)
    guidelinelink =models.CharField(max_length=255,null=True,blank=True)
    faq_link=models.CharField(max_length=255,null=True,blank=True)
    closing_date=models.CharField(max_length=255,null=True,blank=True)
    
 
    def __str__(self):
        return self.scheme_name

class loggers(Scholarship):
    user=models.ManyToManyField(settings.AUTH_USER_MODEL,null=True)
    
    is_selected=models.BooleanField(editable=True,default=False)

    def __str__(self):
        return self.scheme_name
class UserScholarship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'scholarship',)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
