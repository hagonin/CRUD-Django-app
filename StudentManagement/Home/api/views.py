from rest_framework.decorators import api_view
from rest_framework.response import Response

from Home.models import Student
from .serializers import studentSerializer
from Home.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/students',
        'GET /api/students/:student_id',
    ]
    return Response(routes)


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = studentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStudent(request, pk):
    student = Student.objects.get(student_id=pk)
    serializer = studentSerializer(student, many=False)
    return Response(serializer.data)
