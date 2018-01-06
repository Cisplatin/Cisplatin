"""Cisplatin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Cisplatin_App.views import home, blog

urlpatterns = [
    url(r'^$', home.home),
    url(r'^final_testament$', home.final_testament),
    url(r'^genome$', home.genome),
    url(r'^blog$', blog.home),

    url(r'^blog/exploits-using-xlsx-files$', blog.exploits_using_xlsx_files),
    url(r'^robots.txt$', home.robots),
]
