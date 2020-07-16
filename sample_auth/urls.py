from django.urls import path
from sample_auth.views import *

urlpatterns = [
    path('list/', TodoRead.as_view()),
    path('create/', TodoCreate.as_view()),
    path('update/<pk>/', TodoUpdate.as_view()),
    path('delete/<pk>/', TodoDelete.as_view()),
]

