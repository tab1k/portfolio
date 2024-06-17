from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Полное имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Почта'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Сообщение'}))
