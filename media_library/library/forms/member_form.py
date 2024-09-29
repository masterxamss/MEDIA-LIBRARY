from django import forms
from library.models.member_model import Member


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
