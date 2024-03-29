"""The Django docstring."""
from django.db import models
class Employee(models.Model):
    """The Django docstring."""
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        """The Django docstring."""
        db_table = "employee"
        