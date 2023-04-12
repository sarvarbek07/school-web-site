from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class About(models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField(blank=True)
    image=models.ImageField(upload_to="image")

    def __str__(self):
        return self.title

class Teachers(models.Model):
    ismi=models.CharField(max_length=250)
    fani=models.TextField(blank=True)
    rasmi=models.ImageField(upload_to="image")

    def __str__(self):
        return self.ismi


class Blog(models.Model):
    rasm=models.ImageField(upload_to="image_blog",default="image/default.jpg")
    sarlafha=models.CharField(max_length=300)
    matn=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    # foydalanuvchi=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sarlafha
    def get_absolute_url(self):
        return reverse("homepage", kwargs={"pk": self.pk})



