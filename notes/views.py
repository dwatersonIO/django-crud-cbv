from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Note, Tag
from .forms import NoteForm, TagForm


from django.views.generic import (
	ListView,
	CreateView,
	DeleteView,
	UpdateView
)


class NoteList(ListView):
	model = Note
	template_name = 'notes/list_view.html'
	context_object_name = 'notes'
	form_class = NoteForm

	def get_context_data(self, **kwargs):
		context =super().get_context_data(**kwargs)
		context['form'] = self.form_class()
		return context
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid:
			form.save()
			return redirect('/')
		else:
			return render(request.self.template_name, {'form':form})

class FilterList(ListView):
	model = Note
	template_name = 'notes/filter_view.html'
	context_object_name = 'notes'
	form_class = NoteForm

	def get_context_data(self, **kwargs):
		context =super().get_context_data(**kwargs)
		context['form'] = self.form_class()
		return context
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid:
			form.save()
			return redirect('/')
		else:
			return render(request.self.template_name, {'form':form})


class NoteUpdate(UpdateView):
	model=Note
	# fields=['text', 'tags']
	template_name='notes/update_note.html'
	success_url='/'
	form_class = NoteForm


class NoteDelete(DeleteView):
	model=Note
	fields=['text', 'tags']
	template_name='notes/delete_note.html'
	success_url = '/'


