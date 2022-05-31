from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Student
from .serializers import studentSerializer



# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'GET /api',
#         'GET /api/students',
#         'GET /api/students/:id',
#         'POST/api/create'
#     ]
#     return Response(routes) 


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = studentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStudent(request,pk):
    student = Student.objects.get(id=pk)
    serializer = studentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStudent(request):    
    serializer = studentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateStudent(request,pk):    

    student = Student.objects.get(student_id=pk)
    serializer = studentSerializer(instance=student,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteStudent(request,pk):
    student = Student.objects.get(student_id=pk)
    student.delete()
    return Response("You've deleted successfully!")