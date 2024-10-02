from django.db import models
from datetime import date
from home.models import Consultant

# Create your models here.


class CollaborationRequest(models.Model):
    """
    CollaborationRequest model represents a request for collaboration with
    a consultant.

    Attributes:
        cr_id (AutoField): Primary key for the collaboration request.
        consultant_id (ForeignKey): Foreign key to the Consultant model,
                    representing the consultant associated with the request.
        first_name (CharField): First name of the person making the request.
        last_name (CharField): Last name of the person making the request.
        email (EmailField): Email address of the person making the request.
        message (TextField): Message content of the collaboration request.
        request_date (DateTimeField): Timestamp when the request was created,
                    automatically set to the current date and time.
        open (BooleanField): Status of the request, default True (future use).
    Meta:
        ordering (list): Default ordering for the model, sorted by
                         consultant_id, request_date (descending),
                         last_name, and first_name.
    Methods:
        __str__: Returns a string representation of the collaboration request,
                 including consultant_id, last_name, first_name,
                 and request_date.
    """
    cr_id = models.AutoField(primary_key=True)
    consultant_id = models.ForeignKey(
        Consultant, on_delete=models.CASCADE,
        related_name="consultant_collaboration",
        default=1)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.TextField(blank=False)
    request_date = models. DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)  # for future use

    class Meta:
        ordering = ["consultant_id", "-request_date", "last_name",
                    "first_name"]

    def __str__(self):
        return_str = f"{self.consultant_id} | Type: {self.last_name}, "
        return_str += f"{self.first_name} | {self.request_date}"

        return return_str
