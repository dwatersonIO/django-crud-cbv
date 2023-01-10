from django import forms
from django.forms import ModelForm
from notes.models import Note, Tag

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text','tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(choices = Tag.objects.all())
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(choices = Tag.objects.all())
        }
      