from django import forms
from library.models import Dvd


class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = '__all__'
        exclude = ['slug', 'available']
        labels = {
            'title': 'Titre',
            'available': 'Disponible',
            'director': 'Directeur',
            'year': 'Année',
            'writer': 'Réalisateur',
            'rating': 'Note',
            'category': 'Categorie',
            'description': 'Description',
            'image': 'Image'
        }
        error_messages = {
            'title': {
                'required': 'Veuillez renseigner le titre',
                'max_length': 'Limite de caractères dépassée',
            },
            'director': {
                'required': 'Veuillez renseigner le régisseur',
                'max_length': 'Limite de caractères dépassée',
            },
            'year': {
                'required': 'Veuillez renseigner l\'année',
            },
            'writer': {
                'required': 'Veuillez renseigner le rôle',
                'max_length': 'Limite de caractères dépassée',
            },
            'rating': {
                'required': 'Veuillez renseigner la note',
                'min_value': 'La note doit être comprise entre 1 et 5',
                'max_value': 'La note doit être comprise entre 1 et 5',
            },
            'category': {
                'required': 'Veuillez renseigner la catégorie',
                'max_length': 'Limite de caractères dépassée',
            },
            'description': {
                'required': 'Veuillez renseigner la description',
                'max_length': 'Limite de caractères dépassée',
            },
            'image': {
                'filename': 'Veuillez insérer une image valide',
                'error_type': 'format non valide',
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre', 'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'director': forms.TextInput(attrs={'placeholder': 'Directeur', 'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Année', 'class': 'form-control'}),
            'writer': forms.TextInput(attrs={'placeholder': 'Realisateur', 'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Note', 'class': 'form-control'}),
            'category': forms.TextInput(attrs={'placeholder': 'Categorie', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
