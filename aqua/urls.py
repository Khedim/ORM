from django.urls import path
from .views import Add

urlpatterns = [
    path('', Add.as_view())
]
