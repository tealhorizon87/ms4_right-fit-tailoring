from django import forms


class MtmForm(forms.Form):

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
        }

        for field in self.fields:
            if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


    height = forms.CharField(max_length=3, required=False)
    neck = forms.CharField(max_length=3, required=False)
    shoulder = forms.CharField(max_length=3, required=False)
    chest = forms.CharField(max_length=3, required=False)
    arm = forms.CharField(max_length=3, required=False)
    back = forms.CharField(max_length=3, required=False)
    waist = forms.CharField(max_length=3, required=False)
    hips = forms.CharField(max_length=3, required=False)
    leg = forms.CharField(max_length=3, required=False)
    name = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=20)
