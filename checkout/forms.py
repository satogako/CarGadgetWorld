from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('first_name', 'last_name', 'phone', 'email_addres',
                  'country', 'full_address', 'town_city', 'post_code',
                  'order_notes',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Phone Number',
            'email_addres': 'Email Address',
            'country': 'Country / Region',
            'full_address': 'Full address (street, house number, '
                            'apartment number)',
            'town_city': 'Town / City',
            'post_code': 'Post Code',
            'order_notes': 'Notes about your order, e.g. special notes for '
                            'delivery (optional)',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
