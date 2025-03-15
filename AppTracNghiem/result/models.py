#result/models.py
from django.db import models
from django.utils.timezone import now


class Result(models.Model):
    student = models.ForeignKey('user.Student', on_delete=models.CASCADE)  
    score = models.IntegerField()
    total_questions = models.IntegerField() 
    submitted_at = models.DateTimeField(default=now, blank=True)  # Cho phép null


    def __str__(self):
        return f"{self.student} - {self.score} điểm" 