from django import forms
from library.models import Member, Book, Cd, Dvd, MediaReservations

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
        If one of the media fields is filled in, checks if the media is available.
        """
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        dvd = cleaned_data.get('dvd')
        cd = cleaned_data.get('cd')
        member = cleaned_data.get('member')
        member_id = cleaned_data.get('member').id

        if not (book or dvd or cd):
            self.add_error(None, 'Veuillez sélectionner au moins un média (livre, DVD ou CD).')
        else:
            
            if book:
                Book.update_book_available(book.id)
                print('teste book')
            if dvd:
                Dvd.update_dvd_available(dvd.id)
                print('teste dvd')
            if cd:
                Cd.update_cd_available(cd.id)
                print('teste cd')
                
        if member:
            active_reservations = MediaReservations.get_active_reservations(member_id)
            member_bloqued = Member.get_member_blocked(member_id)

            if active_reservations >= 3:
                self.add_error('member', 'Le membre ne peut pas avoir plus de 3 activité en cours.')

            if member_bloqued:
                self.add_error('member', 'Le membre est bloqué. Veuillez contacter l\'administrateur.')

        return cleaned_data