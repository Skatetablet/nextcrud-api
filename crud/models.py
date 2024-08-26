
import uuid
from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)