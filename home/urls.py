from django.urls import path
from .views import IndexView, appView, download_video

urlpatterns = [
    # Defina uma URL separada para download
    path('download/video/', download_video, name='download_video'),
    
    # URL da página de download
    path('', IndexView.as_view(), name='inicio'),
    path('download/', appView.as_view(), name='download'),
    
    
]