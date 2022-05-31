from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.full_name

