from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView ,DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/notes'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/notes'
    form_class = NotesForm
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/notes'
    context_object_name = 'note'
    template_name = 'notes_app/notes_delete.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()
    
def home(request):
    return render(request, 'notes_app/home.html', {})

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class LoginInterfaceView(LoginView):
    template_name = 'notes_app/login.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'notes_app/register.html'
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'notes_app/logout.html'



