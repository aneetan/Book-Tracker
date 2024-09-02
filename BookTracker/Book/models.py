from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    time_mins = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    # order the data (- for inverse) based on new create
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name