"""The Django docstring."""
from django import forms
from employee.models import Employee
class EmployeeForm(forms.ModelForm):
    """The Django docstring."""
    class Meta:
        """The Django docstring."""
        model = Employee
        fields = "__all__"
        