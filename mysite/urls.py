"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    # r'' -> means anything thats not the admin page will go to blog.urls
    #url(r'accounts/login/$', views.login, name='login'),
    #url(r'accounts/logout/$', views.logout, name='logout', kwargs={'next_page':'/'}),
    # this amplies that when you logout then the next page you will go to is the home page i.e. the post list page.
    # path('accounts/login/$', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page':'/'}),
    url(r'accounts/login/$', views.login, name='login'),
    url(r'accounts/logout/$', views.logout, name='logout', kwargs={'next_page':'/'}),
    # it means when you logout you will be redirected to home page.

]
