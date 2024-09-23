from django.db import models
from datetime import date

# Create your models here.

class CollaborationRequest(models.Model):
    cr_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.TextField(blank=False)
    request_date = models. DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-request_date", "last_name","first_name"]

    def __str__(self):
        return f"{self.cr_id} | Type: {self.last_name}, {self.first_name} | {self.request_date}"