from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'subject', 'email', 'message')
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter Message'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter Subject'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Enter your valid email address'
            })
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['subject'].required = True
        self.fields['message'].required = True
