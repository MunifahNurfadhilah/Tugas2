from socket import fromshare
from django import forms

class taskForm(forms.Form):
    title = forms.CharField(label="Judul", max_length=255)
    description = forms.CharField(label="Deskripsi", max_length=255)