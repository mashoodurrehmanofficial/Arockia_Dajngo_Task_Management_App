
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    # path('login/', login_page, name='login'),
    # path('profile/', profile, name='profile'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

