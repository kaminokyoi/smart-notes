from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView, CreateView
from .forms import NotesForm
from .models import Notes
from django.shortcuts import redirect

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes'
    form_class = NotesForm

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'