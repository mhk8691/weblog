from django.db import models

# from Blog.models import Post


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20, default=0)
    image = models.ImageField(
        upload_to="images/User/", blank=True, default="images/User/UserDefult.png"
    )


class Comment(models.Model):
    post = models.ForeignKey("Blog.Post", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
