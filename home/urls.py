from django.urls import path
from .views import IndexView,appView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('download/', appView.as_view(), name='download'),
]