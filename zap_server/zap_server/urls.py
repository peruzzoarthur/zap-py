from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zapp/', include('zapp.urls')),  # Include myapp URLs
]
