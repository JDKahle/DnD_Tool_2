from django.shortcuts import render
from django.shortcuts import HttpResponse
#############################################
from django.http import HttpResponse


from urllib import request
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Person
from django.shortcuts import get_object_or_404

from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

from . import models

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm

from django import forms
# Create your views here.
def simple_view(request):
    return HttpResponse('Hello!')

class PersonHomeView(TemplateView):
    template_name = 'person/home.html'

class PersonCreateView(CreateView):
    model = Person
    # model_form.html --> teacher_form.html
    fields = '__all__'
    success_url = reverse_lazy('person:list_person')

    def form_valid(self, form):     # Alles hier drin ist dafür verantwortlich, 
        obj = form.save(commit=False)   # dass ein sklave automatisch einen owner bekommt.
        obj.owner = self.request.user
        obj.save
        return super().form_valid(form)

class PersonListView(LoginRequiredMixin, ListView):
    model = Person
    context_object_name = "list_of_person"
    queryset = Person.objects.order_by("first_name")


    def get_queryset(self):
        return Person.objects.filter(owner=self.request.user)


class NewPersonBattleListView(LoginRequiredMixin, ListView):
    model = Person
    context_object_name = "list_of_person"
    queryset = Person.objects.order_by("first_name")
    template_name = 'person/person_list_battlex.html'

    def get_queryset(self):
        return Person.objects.filter(owner=self.request.user)


class PersonLvlListView(ListView):
    model = Person
    context_object_name = "list_of_person"
    queryset = Person.objects.order_by("lvl").reverse()


#### Hier hin kommen funktion von den zeilen 87 und 120.


class PersonDetailView(DetailView):
    # model_detail.html
    model = Person


class PersonUpdateView(UpdateView):
    # SHARES model_form.html THAT CREATE VIEW USES
    model = Person
    fields = "__all__"
    widgets = {'owner': forms.HiddenInput()}
    success_url = reverse_lazy('person:list_person')

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('person:list_person')




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'person/signup.html'
