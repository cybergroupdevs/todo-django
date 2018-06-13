from django.db import models

# Create your models here.

class Todo(models.Model):
  text = models.CharField(max_length=100)
  done = models.BooleanField(default=False)

def __str__(self):
  """Return a human readable representation of the model instance."""
  return self.text