from django.db import models


class Student(models.Model):
    student = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=500)

    def __str__(self):
        return "%s %s" % (self.student, self.fullName)


class Grade(models.Model):

    GRADE = (
        ('DJ1221', 'DJ1221'),
        ('JV0222', 'JV0222'),
        ('RE0522', 'RE0522'),
        ('AL0622', 'AL0622'),
    )
    grade = models.AutoField(primary_key=True)
    gradeName = models.CharField(max_length=50, choices=GRADE)

    def __str__(self):
        return self.gradeName


class Subject(models.Model):

    SUBJECT = (
        ('Django web developement', 'Django web developement'),
        ('Javascript', 'Javascript'),
        ('Reactjs', 'Reactjs'),
        ('Algorithme', 'Algorithme'),
        ('HTML & CSS course', 'HTML & CSS course')
    )

    subject = models.AutoField(primary_key=True)
    subjectName = models.CharField(max_length=100, choices=SUBJECT)

    def __str__(self):
        return self.subjectName


class Score(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        db_table = "score"

    def __str__(self):
        return "%s %s %s %s" % (self.student, self.grade, self.subject, self.score)
