
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Notification(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notif_detail", kwargs={"pk": self.pk})


class Complaints(models.Model):

    title = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    descritrion = models.TextField()
    image = models.ImageField(default='default.jpg',
                              upload_to='complaints_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("comp_detail", kwargs={"pk": self.pk})
