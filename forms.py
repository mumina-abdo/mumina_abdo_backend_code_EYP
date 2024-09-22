from django import forms
from .models import MyModel
from django.utils.dateparse import parse_datetime

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['my_datetime']

    def clean_my_datetime(self):
        value = self.cleaned_data['my_datetime']
        if isinstance(value, str):
            parsed_value = parse_datetime(value)
            if parsed_value is None:
                raise forms.ValidationError("Invalid datetime format")
            return parsed_value
        return value