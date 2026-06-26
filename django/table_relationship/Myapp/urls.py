from django.urls import path
from Myapp.views import *

urlpatterns = [
    path('',home,name='home'),
    
    #passport
    path('edit_passport/<int:id>/',edit_passport , name='edit_passport'),
    path('delete_passport/<int:id>/',delete_passport , name='delete_passport'),
    
    #product
    path('edit_product/<int:id>/', edit_product , name='edit_product'),
    path('delete_product/<int:id>/',delete_product , name='delete_product'),
    
    #Author
    path('edit_author/<int:id>/',edit_author ,name='edit_author'),
    path('delete_author/<int:id>/',delete_author , name='delete_author')
]