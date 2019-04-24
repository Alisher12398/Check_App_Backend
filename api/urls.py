from django.urls import path, include
from .views import getQroups
urlpatterns = [
    path('groups/', getQroups),
    # path('task_lists/<int:pk>', taskList_detail),
    # path('task_lists/<int:pk>/tasks/', task_list),
    # path('tasks/<int:pk>/', task_detail)
]