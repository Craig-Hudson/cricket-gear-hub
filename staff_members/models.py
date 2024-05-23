from django.db import models


class StaffMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
