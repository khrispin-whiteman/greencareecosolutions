from django.forms import ModelForm
from django import forms
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor

from greencare.models import Comment, ServicesDeals, Service


class commentsForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name',}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address',}))

    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('name', 'email', 'message', )


class ServiceDealsForm(ModelForm):
    nameofservice = forms.ModelChoiceField(Service.objects.all(),  widget=forms.Select(
                                       attrs={'class': 'form-control btn-block', 'style': 'height: 40px;'}))
    fullName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    phoneNumber = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    description = forms.CharField(widget=FroalaEditor(options={'toolbarInline': True,}))

    class Meta:
        model = ServicesDeals
        fields = ('nameofservice', 'fullName', 'phoneNumber', 'email', 'description', 'accepttermsconditions')