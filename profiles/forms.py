from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_email": "Email",
            "default_phone_number": "Tel",
            "default_address_line_1": "Address line 1",
            "default_address_line_2": "Address line 2",
            "default_city": "City",
            "default_county": "County",
            "default_postcode": "Postcode",
        }

        self.fields['default_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
