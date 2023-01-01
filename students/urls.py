from . import views
from django.urls import path

urlpatterns = [
    path('', views.studentsPage, name='students-page'),
    path('add-student', views.addStudent, name='add-student'),
    path('add-student/add', views.add, name='add'),
    path('add-student/cancel', views.cancel, name='cancel'),
    path('student/<int:id>', views.studentProfile, name='student-profile'),
    path('student/<int:id>/delete', views.deleteStudent, name='delete-student'),
    # path('delete-course/<int:id>', views.deleteCourse, name='delete-course'),
    # path('delete-course/delete/<int:id>', views.delete, name='delete'),
    # path('delete-course/cancel-delete', views.cancelDelete, name='cancel-delete'),
    # path('details/<int:id>', views.details, name='course-details'),
    # path('edit-course/<int:id>', views.editCourse, name='edit-course'),
    # path('edit-course/<int:id>/edit', views.edit, name='edit'),
]