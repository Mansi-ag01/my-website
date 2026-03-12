from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin (Bonus!)
    path('', include('main.urls')),
]
