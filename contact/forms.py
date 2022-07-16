from django import forms
from .models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['article', 'name', 'image', 'email', 'website', 'message']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name