from django.db import models

from Categories.models import Category


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("User.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images/Blog", blank=True)
    is_draft = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
