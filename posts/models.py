from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:30] #displays the first 30 character of the text field.
