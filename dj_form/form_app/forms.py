from django import forms
from .models import employee

class Contact_info(forms.Form):
    name = forms.CharField(label="Your Name", max_length=10)
    email = forms.EmailField()
    number = forms.IntegerField(required = False)

class emp_details(forms.ModelForm):

    class Meta:
        model = employee
        fields = "__all__"
