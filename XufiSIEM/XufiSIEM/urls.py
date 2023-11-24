"""XufiSIEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', views.login, name='login'),
    path('account.html', views.account, name='account'),
    path('', views.index, name='home'),
    path('agentmgmt.html', views.agent, name='agent'),
    path('scan.html', views.scan, name='scan'),
    path('soar.html', views.soar, name='soar'),
    path('soaranalysis.html', views.soaranalysis, name='soaranalysis'),
    path('sbomsecurity.html', views.sbomsecurity, name='sbomsecurity'),
    path('blocklist.html', views.blocklist, name='blocklist'),
    path('agentsettings.html', views.agentsettings, name='agentsettings'),
]
