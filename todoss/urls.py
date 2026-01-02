from django.urls import path
from . import views 

urlpatterns = [
    #Add Task
    path('addTask/' , views.addTask , name='addTask'),
    # Mark as undone
    path('mark_ad_done/<int:pk>/' , views.mark_as_done , name='mark_as_done'),
    # Mark as done
    path('mark_as_undone/<int:pk>/' , views.mark_as_undone, name='mark_as_undone'),
    # For delete
    path('for_delete/<int:pk>/' , views.for_delete, name='for_delete'),
    # For edit
    path('task_edit/<int:pk>/',views.task_edit, name='task_edit'), 
    ]
