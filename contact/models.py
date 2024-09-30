from django.db import models
from datetime import date
from home.models import Consultant

# Create your models here.

class CollaborationRequest(models.Model):
    cr_id = models.AutoField(primary_key=True)
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE, related_name="consultant_collaboration",
        default=1)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.TextField(blank=False)
    request_date = models. DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True) #for future use
    
    class Meta:
        ordering = ["consultant_id", "-request_date", "last_name","first_name"]

    def __str__(self):
        return f"{self.consultant_id} | Type: {self.last_name}, {self.first_name} | {self.request_date}"