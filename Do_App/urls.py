from django.urls import path

from . import views

app_name = 'Do_App'

urlpatterns=[
    path('', views.index, name="index"),        #root url in which user comes to this url first when opens
    path('addTask', views.addTask, name="addTask"),
    path('deleteTask/<int:id>', views.deleteTask, name='deleteTask'),
    path('completedTask/<int:id>', views.completedTask, name ="completedTask"),
    path('updatedTask/<int:id>', views.updatedTask, name='updatedTask'),
    path('deleteAllCompleted', views.deleteAllCompleted, name='deleteAllCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
]