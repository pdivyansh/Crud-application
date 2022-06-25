from unicodedata import name
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('insert',views.insert,name="insert"),
    path('insertdata',views.InsertData,name='insertdata'),
    path('show',views.show,name='show'),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('updatedata/<int:pk>',views.UpdateData,name="updatedata"),
    path('Ddeketedata/<int:pk>',views.DeleteData,name="deletedata"),
]