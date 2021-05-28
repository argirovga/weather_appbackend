from django.contrib import admin
from django.urls import path, include
from personal_api.views import view_available_requests
from personal_api.views import view_documentation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('personal_api.urls', namespace='api'), name='api'),
    path('', view_available_requests, name='starting_page'),
]