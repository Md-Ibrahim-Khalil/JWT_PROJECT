from django.contrib import admin
from django.urls import path, include
from products.urls import DemoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jwt_app.urls')),
    path('api/jwt_app', include('jwt_app.urls')),
    path('api/', include("products.urls")),
]