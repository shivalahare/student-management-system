from django.db import models
from django.contrib.auth.models import User

# Extend the default User model if needed
class CustomUser(User):
    role = models.CharField(max_length=50)  # e.g., 'student', 'teacher', 'admin'

# Student model
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    enrollment_date = models.DateField()
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    batch = models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True, related_name='students')
    profile_picture = models.ImageField(upload_to='profiles/')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE ,null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Teacher model
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    # subjects = models.ManyToManyField('Course')
    profile_picture = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    instructor = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# Batch model
class Batch(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # No change needed here if related_name is set in Student model

    def __str__(self):
        return self.name

# Attendance model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # 'Present' or 'Absent'

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

# Fee model
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10)  # 'Paid' or 'Unpaid'

    def __str__(self):
        return f"{self.student} - {self.amount} - {self.status}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name