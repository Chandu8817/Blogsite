from django.db import models

# Create your models here.



class BlogDetial(models.Model):

    bg_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=1000)
    blog_img=models.ImageField(upload_to='images/')
    pub_date=models.DateTimeField()