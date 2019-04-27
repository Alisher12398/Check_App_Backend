from django.urls import path, include
from .views import getQroups, getQa, getQaG, getUserPoints, getUser, getUserGroupPoints, checkPassword
urlpatterns = [
    path('groups/', getQroups),
    path('questions/<int:pk>', getQa),
    path('groups/<int:pk>/questions/', getQaG),
    path('user/<str:nameTemp>/points/', getUserPoints),
    path('user/<str:nameTemp>/', getUser),
    path('user/<int:idUserTemp>/group/<int:pk>/', getUserGroupPoints),
    path('user/<str:nameTemp>/check/<str:passwordTemp>/', checkPassword),
]