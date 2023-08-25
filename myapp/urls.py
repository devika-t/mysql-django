from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('userreg/',views.userreg,name="userreg"),
    path('insertuser/',views.insertuser,name="insertuser"),
    path('delete/<int:uid>/', views.delete, name="delete"),
    path('update/<int:uid>/',views.update, name="update"),
    path('update/uprec/<int:uid>/',views.uprec, name="uprec"),
]