from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher, Course, Batch, Attendance, Fee
from .forms import StudentForm, TeacherForm, CourseForm, BatchForm, AttendanceForm, FeeForm



def home(request):
    return render(request, 'student_app/home.html')
def dashboard(request):
    return render(request, 'student_app/dashboard.html')
# Student views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_app/student_detail.html', {'student': student})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_app/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_app/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/student_confirm_delete.html', {'student': student})

# Teacher views
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'student_app/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'student_app/teacher_detail.html', {'teacher': teacher})

def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'student_app/teacher_form.html', {'form': form})

def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'student_app/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'student_app/teacher_confirm_delete.html', {'teacher': teacher})
# Similar views for Teacher, Course, Batch, Attendance, Fee...

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'student_app/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'student_app/course_detail.html', {'course': course})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'student_app/course_form.html', {'form': form})

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'student_app/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'student_app/course_confirm_delete.html', {'course': course})

# Similar views for Teacher, Course, Batch, Attendance, Fee...

def batch_list(request):
    batches = Batch.objects.all()
    return render(request, 'student_app/batch_list.html', {'batches': batches})

def batch_detail(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    return render(request, 'student_app/batch_detail.html', {'batch': batch})

def batch_add(request):
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm()
    return render(request, 'student_app/batch_form.html', {'form': form})

def batch_edit(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('batch_detail', pk=batch.pk)
    else:
        form = BatchForm(instance=batch)
    return render(request, 'student_app/batch_form.html', {'form': form})

def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        batch.delete()
        return redirect('batch_list')
    return render(request, 'student_app/batch_confirm_delete.html', {'batch': batch})