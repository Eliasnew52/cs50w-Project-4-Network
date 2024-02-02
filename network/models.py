from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    Content = models.CharField(max_length=400)
    Author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Author")
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} made by {self.Author} on {self.Date.strftime('%d %b %Y %H:%M:%M:%S')}"