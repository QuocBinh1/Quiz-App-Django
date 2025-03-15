#quiz/views.py
from django.shortcuts import render, redirect
from .models import Question, Answer 
from result.models import Result
from user.models import Student
def quiz(request):
    studentId = request.session.get("studentId")
    
    if not studentId:
        return redirect("login")  # Nếu chưa đăng nhập, chuyển về trang login
    
    questions = Question.objects.prefetch_related("answers").all()
    
    return render(request, 'quiz/quiz.html' , {'questions': questions})
def submit_quiz(request):
    studentId = request.session.get("studentId")
    
    if not studentId:
        return redirect("login")  # Nếu chưa đăng nhập, chuyển về trang login

    if request.method == "POST":
        score = 0  # Biến lưu điểm số
        total_questions = Question.objects.count()  # Đếm tổng số câu hỏi
        
        for question in Question.objects.all():
            selected_answer_id = request.POST.get(f"question_{question.id}")  # Lấy đáp án từ form
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:  # Kiểm tra đáp án đúng
                    score += 1

        # Lưu kết quả vào database
        student = Student.objects.get(studentId=studentId)
        result = Result.objects.create(student=student, score=score, total_questions=total_questions)

        return redirect("result", studentId=student.studentId)  # Chuyển hướng đến trang kết quả

    return redirect("quiz")