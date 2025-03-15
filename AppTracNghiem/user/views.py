from django.shortcuts import render , redirect
from .models import Student  # Import model

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def submit_login(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullName')
        studentId = request.POST.get('studentId')
        email = request.POST.get('email')

        student, created = Student.objects.get_or_create(
            studentId=studentId, 
            defaults={'fullName': fullname, 'email': email} 
        )
        request.session["studentId"] = studentId
        
      
        return redirect('quiz')
    return redirect('login')
        

