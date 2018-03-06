from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from .models import *
from .forms import *

# Create your views here.

MODELS = ('Quest',)

class AddQuestView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddQuestForm(initial={"creator":User.username})
        return render(request, "add_quest.html", {"form": form})

    def post(self, request):
        form = AddQuestForm(request.POST)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.creator = request.user
            quest.save()
            return redirect("/add_quest")

class QuestSearchView(LoginRequiredMixin, View):
    def get(self, request):
        form = QuestSearchForm()
        ctx = {'form':form}
        return render(request, "quests.html", ctx)

    def post(self, request):
        form = QuestSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quests = Quest.objects.filter(name__icontains=name)

            ctx = {
                'form': form,
                'quests': quests,
            }
            return render(request, "quests.html", ctx)
        return redirect("quests")

class ShowQuestView(LoginRequiredMixin, View):
    def get(self, request, quest_id):
        try:
            quest = Quest.objects.get(pk=quest_id)
        except quest.DoesNotExist:
            quest = None

        ctx = {
            "quest": quest,
        }
        return render(request, "show_quest.html", ctx)

class ToDoView(View):
    def get(self, request):
        return render(request, "todo.html")

class FeaturesView(View):
    def get(self, request):
        return render(request, "features.html")

class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            url = request.GET.get("next")
            return redirect(url)

        return HttpResponse("Error")


def my_logout(request):
    logout(request)
    return HttpResponse("wylogowano")
'''
class AddDomainView(View):

    def get(self, request):
        form = AddDomainForm()
        return render(request, "add_domain.html", {"form": form})

    def post(self, request):
        form = AddDomainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/add_domain")
'''
# class AddComponentView(View):
#
#     def get(self, request):
#         form = AddComponentForm()
#         return render(request, "add_component.html", {"form": form})
#
#     def post(self, request):
#         form = AddComponentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/add_component")
#
# class AddEquipmentView(View):
#
#     def get(self, request):
#         form = AddEquipmentForm()
#         return render(request, "add_equipment.html", {"form": form})
#
#     def post(self, request):
#         form = AddEquipmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/add_equipment")


class ShowMainView(View):
    def get(self, request):
        return render(request, "index.html", {"form":form})


