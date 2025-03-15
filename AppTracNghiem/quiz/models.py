from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"Câu {self.order}: {self.question_text}"
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")  
    answer_text = models.CharField(max_length=255)  
    is_correct = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.answer_text} ({'Đúng' if self.is_correct else 'Sai'})"
