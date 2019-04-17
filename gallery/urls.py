from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url('^$',views.index,name ='home'),
    url(r'^search/', views.search, name='search_images'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),
    url(r'^image/(\d+)',views.single_image, name='art'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

