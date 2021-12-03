"""Consumer_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from studentsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('students/', views.StudentListView,
         name='student_list'),

    path('students/<int:pk>/detail/', views.StudentDetailView,
         name='student_detail'),

    path('students/<int:pk>/delete/', views.StudentDeleteView,
         name='student_delete'),

    path('students/create/', views.StudentCreateView,
         name='student_create'),

    path('students/<int:pk>/update/', views.StudentUpdateView,
         name='student_update'),

]







