
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('insert_new_chore/', insert_new_chore, name='insert_new_chore'),
    path('insert_new_transaction/', insert_new_transaction, name='insert_new_transaction'),
    path('test/', test, name='test'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

