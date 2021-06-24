"""CNproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from DeskShare.views import upload_pdf, \
    deskSharePage, register_page, login_page,\
    logout_user,email_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('DeskShare/logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('DeskShare/upload/', upload_pdf, name='upload'),
    path('DeskShare/', deskSharePage, name='DeskShare'),
    path('DeskShare/share/',email_view,name = 'share')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
