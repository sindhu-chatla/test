
from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'address','destination','tags']
        fields = "__all__"
        widgets = {
            'destination': forms.Select(),
            'tags': forms.CheckboxSelectMultiple()
        }