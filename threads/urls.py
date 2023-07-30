from django.urls import path
from .views import *
urlpatterns = [
    path('',main),
    path('threads/<int:thread_id>',thread),
    path('new',new_thread)
]

