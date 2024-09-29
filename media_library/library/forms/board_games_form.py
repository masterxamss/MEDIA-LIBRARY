from django import forms
from library.models import BoardGame


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'
        book_image = forms.ImageField()
        exclude = ['slug']
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
