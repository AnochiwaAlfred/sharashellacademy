from . import views
from django.urls import path

urlpatterns = [
    path('', views.department, name='department'),
    path('add-department', views.addDepartment, name='add-department'),
    path('add-department/add', views.add, name='add'),
    path('add-department/cancel', views.cancel, name='cancel'),
    path('delete-department/<int:id>', views.deleteDepartment, name='delete-department'),
    path('delete-department/delete/<int:id>', views.delete, name='delete'),
    path('delete-department/cancel-delete', views.cancelDelete, name='cancel-delete'),
    path('details/<int:id>', views.details, name='department-details'),
    path('edit-department/<int:id>', views.editDepartment, name='edit-department'),
    path('edit-department/<int:id>/edit', views.edit, name='edit'),
]