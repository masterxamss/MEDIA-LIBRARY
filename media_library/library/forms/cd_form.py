from django import forms
from library.models import Cd


class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = '__all__'
        book_image = forms.ImageField()
        exclude = ['slug', 'available']
        labels = {
            'title': 'Titre',
            'available': 'Disponible',
            'artist': 'Artiste',
            'album': 'Album',
            'year': 'Année',
            'genre': 'Genre',
            'description': 'Description'
        }
        error_messages = {
            'title': {
                'required': 'Veuillez renseigner le titre',
                'max_length': 'Limite de caractères dépassée'
            },
            'artist': {
                'required': 'Veuillez renseigner l\'artiste',
                'max_length': 'Limite de caractères dépassée'
            },
            'album': {
                'required': 'Veuillez renseigner l\'album',
                'max_length': 'Limite de caractères dépassée'
            },
            'year': {
                'required': 'Veuillez renseigner l\'annee',
            },
            'genre': {
                'required': 'Veuillez renseigner le genre',
                'max_length': 'Limite de caractères dépassée'
            },
            'description': {
                'max_length': 'Limite de caractères dépassée'
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du CD', 'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artiste du CD', 'class': 'form-control'}),
            'album': forms.TextInput(attrs={'placeholder': 'Album du CD', 'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Année du CD', 'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre du CD', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description du CD', 'class': 'form-control'})
        }
