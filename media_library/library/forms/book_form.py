from django import forms
from library.models import Book

# -----------------------------------------------------------
# FORM BOOK
# -----------------------------------------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['slug', 'available']
        labels = {
            'title': 'Titre',
            'author': 'Auteur',
            'pages': 'Pages',
            'language': 'Langue',
            'release_date': 'Date de sortie',
            'publisher': 'Editeur'

        }
        error_messages = {
            'title': {
                'required': 'Veuillez renseigner le titre',
                'max_length': 'Limite de caractères dépassée'
            },
            'author': {
                'required': 'Veuillez renseigner l\'auteur',
                'max_length': 'Limite de caractères dépassée'
            },
            'pages': {
                'required': 'Veuillez renseigner le nombre de pages',
            },
            'language': {
                'required': 'Veuillez renseigner la langue',
                'max_length': 'Limite de caractères dépassée'
            },
            'release_date': {
                'required': 'Veuillez renseigner la date de sortie',
                'invalid': 'Veuillez entrer une date valide (format AAAA-MM-JJ)'
            },
            'publisher': {
                'required': 'Veuillez renseigner l\'editeur',
                'max_length': 'Limite de caractères dépassée'
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du livre', 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'placeholder': 'Auteur du livre', 'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'placeholder': 'Nombre de pages', 'class': 'form-control'}),
            'language': forms.TextInput(attrs={'placeholder': 'Langue du livre', 'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'placeholder': 'Date de sortie', 'class': 'form-control', 'type': 'date'}),
            'publisher': forms.TextInput(attrs={'placeholder': 'Editeur du livre', 'class': 'form-control'})
        }