from django.urls import path
from notes import views

urlpatterns = [
	path('', views.NoteList.as_view(), name="list_view"),
	path('filter/', views.FilterList.as_view(), name="filter_view"),
	path('update_note/<str:pk>/',views.NoteUpdate.as_view(), name="update_note"),
	path('delete/<str:pk>/', views.NoteDelete.as_view(), name="delete_note"),
]