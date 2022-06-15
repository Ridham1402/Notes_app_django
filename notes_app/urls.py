from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage '),
    path('notes/', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='notes.detail'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

]
