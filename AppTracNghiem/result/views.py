from django.shortcuts import render, redirect
from .models import Result
from user.models import Student

def result(request, studentId):
    try:
        # Lấy thông tin sinh viên
        student = Student.objects.get(studentId=studentId)
        results = Result.objects.filter(student=student).order_by("-submitted_at")
    except Student.DoesNotExist:
        return redirect("quiz")  

    return render(request, "result/result.html", {
        "student": student,
        "results": results
    })
