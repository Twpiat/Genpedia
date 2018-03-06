"""Genpedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from Genpedia_portal_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^/', ShowMainView.as_view()),
    url(r'^add_quest/', AddQuestView.as_view()),
    # url(r'^add_component/',AddComponentView.as_view()),
    # url(r'^add_equipment/', AddEquipmentView.as_view()),
    # url(r'^add_domain/', AddDomainView.as_view()),
    url(r'^quests/', QuestSearchView.as_view()),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'show_quest/(?P<quest_id>\d)+', ShowQuestView.as_view(), name='show_quest'),
    url(r'^logout/$', my_logout),
    url(r'^todo', ToDoView.as_view()),
    url(r'^features', FeaturesView.as_view()),

]
