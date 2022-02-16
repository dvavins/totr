from django import forms

from account.models import Account


class UserRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Create Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Password must match')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Your First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Your Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = ''



class SigninForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))

