from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    sender = forms.EmailField(max_length=40, label='Email')
    subject = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=500)
    message = forms.CharField(widget=forms.Textarea)
