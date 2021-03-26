from django import forms
from .models import PT


class PTForm(forms.ModelForm):
    class Meta:
        model = PT
        fields = (
            'full_name', 'slug', 'opening_statement', 'description',
            'availability', 'contact_number', 'PT_image'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].widget.attrs['pattern'] = "[^' ']+"
