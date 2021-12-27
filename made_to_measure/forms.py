from django import forms
from .models import MtmOrder


class MtmForm(forms.ModelForm):
    class Meta:
        model = MtmOrder
        fields = ("name", "email", "phone","height",
                  "neck", "shoulder", "chest",
                  "arm", "back", "waist", "hips", "leg",
                  "garment", "product", "order_total")

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "height": "Height",
            "neck": "Neck",
            "shoulder": "Shoulder Width",
            "chest": "Chest",
            "arm": "Arm Length",
            "back": "Back",
            "waist": "Waist",
            "hips": "Hips",
            "leg": "Inside Leg",
            "name": "Full Name",
            "email": "Email",
            "phone": "Tel",
            "garment": "gamrent",
            "product": "product",
            "order_total": "order_total",
        }

        for field in self.fields:
            if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
