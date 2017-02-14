from django.db import models
from django.core.urlresolvers import reverse

class File(models.Model):
    file_name = models.FileField(upload_to='media/')
# Create your models here.
