from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(
		label = 'نا کاربری',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'نام کاربری',
			}
		)
	)
	password = forms.CharField(
		label = 'رمز عبور',
		widget = forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'رمز عبور',
			}
		)
	)

class UserEditForm(forms.Form):
	username = forms.CharField(
		label = '',
		widget = forms.TextInput(
			attrs = {
				'class' : 'form-control',
				'placeholder' : '',
			}
		)
	)