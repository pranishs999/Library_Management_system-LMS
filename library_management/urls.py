from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Custom admin URL (hidden from /admin/)
    path('lib-control-panel/', admin.site.urls),
    # Auth (login, signup, logout, settings)
    path('auth/', include('library.auth_urls')),
    # Main library app
    path('', include('library.urls')),
]
