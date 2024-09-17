from django import forms
from .models import Member, BoardGame, Book, Cd, Dvd, MediaRequests

# -----------------------------------------------------------
# FORM MEMBERS
# -----------------------------------------------------------


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Email',
            'phone': 'Téléphone',
            'blocked': 'Bloqué',
            'street': 'Rue',
            'postal_code': 'Code postal',
            'city': 'Ville'
        }
        error_messages = {
            'first_name': {
                'required': 'Veuillez renseigner votre prénom',
                'max_length': 'Limite de caractères dépassée',
            },
            'last_name': {
                'required': 'Veuillez renseigner votre nom',
                'max_length': 'Limite de caractères dépassée',
            },
            'email': {
                'required': 'Veuillez renseigner votre email',
            },
            'phone': {
                'required': 'Veuillez renseigner votre téléphone',
                'max_length': 'Limite de caractères dépassée',
            },
            'street': {
                'required': 'Veuillez renseigner votre rue',
                'max_length': 'Limite de caractères dépassée',
            },
            'postal_code': {
                'required': 'Veuillez renseigner votre code postal',
                'max_length': 'Limite de caractères dépassée',
            },
            'city': {
                'required': 'Veuillez renseigner votre ville',
                'max_length': 'Limite de caractères dépassée'
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Votre Prénom', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Votre Nom', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'mail@mail.com', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '06 00 00 00 00', 'class': 'form-control'}),
            'blocked': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'placeholder': 'Rue de Metz', 'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'placeholder': '57000', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Metz', 'class': 'form-control'})
        }


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'
        labels = {
            'name': 'Nom',
            'creator': 'Créateur'
        }
        error_messages = {
            'name': {
                'required': 'Veuillez renseigner le nom',
                'max_length': 'Limite de caractères dépassée'
            },
            'creator': {
                'required': 'Veuillez renseigner le créateur',
                'max_length': 'Limite de caractères dépassée'
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom du jeu', 'class': 'form-control'}),
            'creator': forms.TextInput(attrs={'placeholder': 'Nom du créateur', 'class': 'form-control'})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Titre',
            'available': 'Disponible',
            'author': 'Auteur',
            'pages': 'Pages',
            'language': 'Langue',
            'realease_date': 'Date de sortie',
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
            'realease_date': {
                'required': 'Veuillez renseigner la date de sortie',
            },
            'publisher': {
                'required': 'Veuillez renseigner l\'editeur',
                'max_length': 'Limite de caractères dépassée'
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du livre', 'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'placeholder': 'Auteur du livre', 'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'placeholder': 'Nombre de pages', 'class': 'form-control'}),
            'language': forms.TextInput(attrs={'placeholder': 'Langue du livre', 'class': 'form-control'}),
            'realease_date': forms.DateInput(attrs={'placeholder': 'Date de sortie', 'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'placeholder': 'Editeur du livre', 'class': 'form-control'})
        }


class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = '__all__'
        labels = {
            'title': 'Titre',
            'available': 'Disponible',
            'artist': 'Artiste',
            'album': 'Album',
            'year': 'Année',
            'genre': 'Genre'
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
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du CD', 'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artiste du CD', 'class': 'form-control'}),
            'album': forms.TextInput(attrs={'placeholder': 'Album du CD', 'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Année du CD', 'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre du CD', 'class': 'form-control'})
        }


class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = '__all__'
        labels = {
            'title': 'Titre',
            'available': 'Disponible',
            'director': 'Directeur',
            'year': 'Année',
            'writer': 'Réalisateur',
            'rating': 'Note',
            'category': 'Categorie',
            'description': 'Description'
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
            },
            'category': {
                'required': 'Veuillez renseigner la catégorie',
                'max_length': 'Limite de caractères dépassée',
            },
            'description': {
                'required': 'Veuillez renseigner la description',
                'max_length': 'Limite de caractères dépassée',
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
        }


class MediaRequestsForm(forms.ModelForm):
    class Meta:
        model = MediaRequests
        fields = '__all__'
        error_messages = {
            'member': {
                'required': 'Veuillez renseigner le membre',
            },
            'book': {
                'required': 'Veuillez renseigner le livre',
            },
            'dvd': {
                'required': 'Veuillez renseigner le DVD',
            },
            'cd': {
                'required': 'Veuillez renseigner le CD',
            },
        }
        widgets = {
            'member': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.ModelChoiceField(queryset=Book.objects.filter(available=True), widget=forms.Select(attrs={'class': 'form-control'})),
            'dvd': forms.ModelChoiceField(queryset=Dvd.objects.filter(available=True), widget=forms.Select(attrs={'class': 'form-control'})),
            'cd': forms.ModelChoiceField(queryset=Cd.objects.filter(available=True), widget=forms.Select(attrs={'class': 'form-control'})),
            'date_requested': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'returned': forms.CheckboxInput(attrs={'class': 'form-control', 'type': 'checkbox'}),
            'date_returned': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
