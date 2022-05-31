
from django.urls import path
from . import views

urlpatterns = [
    path('student',views.student,name ='home'),
    path('show/',views.show,name ='show'),
    path('edit/<str:id>/',views.edit,name ='edit'),
    path('update/<str:id>',views.update,name ='update'),
    path('delete/<str:id>',views.clear,name ='delete')

]