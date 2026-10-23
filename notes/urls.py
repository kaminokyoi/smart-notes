from django.urls import path

from .views import NoteListView, NoteDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView, SignupView

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note.list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note.detail'),
    path('notes/new', NotesCreateView.as_view(), name='note.new'),
    path('notes/<int:pk>/edit/', NotesUpdateView.as_view(), name='note.update'),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view(), name='note.delete'),
    path('signup/', SignupView.as_view(), name='signup'),
]