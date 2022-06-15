from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'description', 'tags') 
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-3'}),
            'description': forms.Textarea(attrs={'class':'form-control my-3'}),
            'tags': forms.TextInput(attrs={'class':'form-control my-3'}),
        }
