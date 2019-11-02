from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter UserName'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter Password'})
    )


class SignUpForm(forms.Form):

    first_name = forms.CharField(
        required=True,
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter FirstName'})
    )
    last_name = forms.CharField(
        required=True,
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter LastName'})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter UserName'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter Password'})
    )