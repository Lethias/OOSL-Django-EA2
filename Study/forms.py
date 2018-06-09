from django.forms import *
from Study.models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['lastname', 'firstname', 'email', 'studiengang', 'module']
        labels = {
            "lastname": "Nachname",
            "firstname": "Vorname",
            "email": "Email",
            "studiengang": "Studiengang",
            "module": "Module",
        }
