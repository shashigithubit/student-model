from django.shortcuts import render, get_object_or_404
from .models import Student, SubjectMarks

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    subject_marks = SubjectMarks.objects.filter(student=student)
    return render(request, 'students/student_detail.html', {'student': student, 'subject_marks': subject_marks})
