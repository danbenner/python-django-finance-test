
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('debt/', include('debt.urls')),
    path('insurance/', include('insurance.urls')),
    path('savings/', include('savings.urls')),
    path('spending/', include('spending.urls')),
    path('taxes/', include('taxes.urls')),
    path('admin/', admin.site.urls),
]
