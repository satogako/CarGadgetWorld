from django import forms
from .models import Product, Category, Brand, Catalogue


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()

        friendly_names_category = [(c.id, c.get_display_name()) for c in categories]
        friendly_names_brands = [(c.id, c.get_display_name()) for c in brands]

        self.fields['category'].choices = friendly_names_category
        self.fields['brand'].choices = friendly_names_brands