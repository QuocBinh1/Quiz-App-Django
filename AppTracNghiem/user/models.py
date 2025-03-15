from django.db import models

class Student(models.Model):
    fullName = models.CharField(max_length=150)
    studentId = models.CharField(max_length=128, primary_key=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.fullName} ({self.studentId})"
