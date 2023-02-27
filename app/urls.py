from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_detail/<str:id>', views.portfolio_detail, name='portfolio_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)