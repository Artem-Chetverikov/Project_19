from django import forms

class UseForm(forms.Form):
    username_dj = forms.CharField(max_length=30, label='Введите логин', required=False)
    password_dj = forms.CharField(min_length=8, label='Введите пароль', required=False)
    repeat_password_dj = forms.CharField(min_length=8, label='Повторите пароль', required=False)
    age_dj = forms.IntegerField(max_value=999, min_value=18, label='Введите свой возраст', required=False)
