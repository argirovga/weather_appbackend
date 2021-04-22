from django.contrib import admin
from django.urls import path, include
from personal_api.views import view_available_requests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('personal_api.urls')),
    path('', view_available_requests),
]