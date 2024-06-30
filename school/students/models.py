from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubjectMarks(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)  # Correct reference
    language1 = models.IntegerField()
    language2 = models.IntegerField()
    acting = models.IntegerField()
    dance = models.IntegerField()

    def __str__(self):
        return f"{self.student.name}'s Marks"
