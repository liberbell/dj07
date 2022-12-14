from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")
    body = models.TextField(max_length=1024)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]