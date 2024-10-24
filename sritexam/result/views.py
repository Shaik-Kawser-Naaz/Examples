from django.shortcuts import render

 
# Create your views here.
def student(request):
    students = {
        3244: {'name': 'Lahari', 'pass_subjects': 4, 'fail_subjects': 'Computer Science', 'semester': 7},
    }
    student = None
    if request.method == "POST":
        student_id = request.POST.get('n5')
        if student_id:
            student_id = int(student_id)
            student = students.get(student_id)

    return render(request, 'student.html', {'student':student})