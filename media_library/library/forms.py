from django import forms
from django.core.exceptions import ValidationError
from . models import Member, BoardGame, Book, Cd, Dvd, MediaReservations

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

# -----------------------------------------------------------
# FORM BOARD GAMES
# -----------------------------------------------------------


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


# -----------------------------------------------------------
# FORM CD
# -----------------------------------------------------------
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


# -----------------------------------------------------------
# FORM DVD
# -----------------------------------------------------------
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


# -----------------------------------------------------------
# FORM MEDIA REQUEST
# -----------------------------------------------------------
class MediaReservationsForm(forms.ModelForm):
    class Meta:
        model = MediaReservations
        fields = '__all__'
        exclude = ['returned', 'date_returned']
        labels = {
            'date_requested': 'Date de requête',
            'date_due': 'Date de retournement',
        }

        widgets = {
            'date_requested': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'true'}),
            'date_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'true'}),
        }

    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Sélectionner un membre',
        label='Membre',
        error_messages={'required': 'Veuillez renseigner le membre'}
    )

    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(available=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sélectionner un livre",
        required=False,
        label='Livre'
    )
    
    dvd = forms.ModelChoiceField(
        queryset=Dvd.objects.filter(available=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sélectionner un dvd",
        required=False,
        label='Dvd'
    )
    
    cd = forms.ModelChoiceField(
        queryset=Cd.objects.filter(available=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sélectionner un cd",
        required=False,
        label='Cd'
    )
    
    def clean(self):
        """
        Checks if a member already has 3 active reservations.
        If so, adds an error for the member.
        Checks if one of the media fields (book, DVD or CD) has been filled in.
        If not, adds an error.
        """
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        dvd = cleaned_data.get('dvd')
        cd = cleaned_data.get('cd')
        member = cleaned_data.get('member')
        member_id = cleaned_data.get('member').id

        if not (book or dvd or cd):
            self.add_error(None, 'Veuillez sélectionner au moins un média (livre, DVD ou CD).')
        
        if member:
            active_reservations = MediaReservations.objects.filter(member=member, returned=False).count()
            member_bloqued = Member.objects.filter(id=member_id, blocked=True).exists()
            if active_reservations >= 3:
                self.add_error('member', 'Le membre ne peut pas avoir plus de 3 activité en cours.')
            if member_bloqued:
                self.add_error('member', 'Le membre est bloqué. Veuillez contacter l\'administrateur.')

        return cleaned_data
