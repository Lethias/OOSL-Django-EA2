from django.db import models


class Studiengang(models.Model):
    studiengangname = models.CharField(max_length=20)
    fachbereich = models.CharField(max_length=20)

    def __str__(self):
        return self.studiengangname


class Modul(models.Model):
    modulname = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    semester = models.IntegerField()
    ects = models.IntegerField()

    def __str__(self):
        return self.modulname


class Student(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, blank=True)
    studiengang = models.ForeignKey(Studiengang, on_delete=models.CASCADE)
    module = models.ManyToManyField(Modul, blank=True)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)
