from django.db import models

#Autoincrement and autoassign User ID
def AssignID():
    largest = User.objects.all().order_by('user_id').last()
    id = str(largest)
    number = int(id[-1]) + 1
    new_id = "U0000" + str(number)
    return new_id

#Diagnostic Model
class Diagnostic (models.Model):
    diagnostic = models.CharField(primary_key = True, max_length = 6)
    question_1 = models.CharField(max_length = 30)
    question_2 = models.CharField(max_length = 30)
    question_3 = models.CharField(max_length = 30)
    question_4 = models.CharField(max_length = 30)
    question_5 = models.CharField(max_length = 30)
    question_6 = models.CharField(max_length = 30)

#User Model
class User(models.Model):
    user_id = models.CharField(primary_key = True, max_length = 10, default = AssignID)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    is_staff = models.BooleanField(default = False)

    def __str__(self):
        return self.user_id

#Programme Model
class Programme(models.Model):
    programme_id = models.CharField(primary_key = True, max_length = 10)
    programme_name = models.CharField(max_length = 70)

    def __str__(self):
        return self.programme_name

#Course Model
class Course (models.Model):
    course_id = models.CharField(primary_key = True, max_length = 10)
    course_name = models.CharField(max_length = 70)
    is_supplementary = models.BooleanField(default = True)

    def __str__(self):
        return self.course_id

#Student Model
class Student(models.Model):
    user_id = models. ForeignKey(User, on_delete = models.CASCADE)
    programme_id = models.ForeignKey(Programme, on_delete = models.CASCADE, null = True)
    starting_score = models.IntegerField(null = True)
    final_score = models.IntegerField(null = True)

    #def __str__(self):
    #    return self.

#Courses Assigned to Students / Composite Table
class AssignedCourses(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    progress = models.IntegerField(default = 0)

    #def __str__(self):
    #    return self.course_id)

#Courses Assigned ot Programmes / Composite Table
class ProgrammeCourses(models.Model):
    programme_id = models.ForeignKey(Programme, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)





