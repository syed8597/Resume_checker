from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('users.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('resumes/', include('resumes.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
