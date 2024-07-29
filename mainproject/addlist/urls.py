from django.urls import path
from django.urls import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('businessman_panellogin',views.businessmanpanellogin,name="businessman_panellogin"),
    path('businessmanpanel',views.businessmanpanel,name="businessmanpanel"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('deleteproduct',views.deleteproduct,name="deleteproduct"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)