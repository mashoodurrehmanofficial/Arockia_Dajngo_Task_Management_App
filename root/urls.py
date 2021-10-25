
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
      
      
    path('', index, name='index'), 
    path('home/', index, name='index'), 
    path('all_chore_list/', all_chore_list, name='all_chore_list'), 
    
    
    path('points_cart_add/', points_cart_add, name='points_cart_add'), 
    path('points_cart_delete/', points_cart_delete, name='points_cart_delete'), 
    path('submit_chores/', submit_chores, name='submit_chores'), 
 
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

