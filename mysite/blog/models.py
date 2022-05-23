from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return  self.category_name
class Post(models.Model):
    header_text = models.CharField(max_length=200)
    content_text = RichTextField(blank=True, null = True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=4)
    image = models.ImageField(upload_to= 'blogImages/', default='default.jpg')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return  self.header_text



