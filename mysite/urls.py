"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from helloapp import views
from . import testdb, search, search2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index2/', include('hello2app.urls')),
    path('index/', views.hello),
    path('testdb/', testdb.testdb),
    path('search-form/', search.search_form),
    path('search-form/search/', search.search),
    path('search-post', search2.search_post),

    path('web/', include(('web.urls', 'web'))),
    path('sms/', views.sms),
]


