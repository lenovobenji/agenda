from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    """Contact object"""

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    user = models.ForeignKey(User,related_name="contacts",on_delete=models.PROTECT)
    
    
    def __str__(self) -> str:
        return self.name