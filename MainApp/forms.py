from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput
from django.core.exceptions import ValidationError


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'public', ]
        labels = {'name': 'Название', 'lang': 'Язык прграммирования', 'code': 'Пример кода на языке',}
        widgets = {
                  'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
                  'code': Textarea(attrs={'placeholder': 'Код сниппета'}),
        }

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]

    password_1 = CharField(label='password', widget=PasswordInput)
    password_2 = CharField(label='password confirm', widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 3:     # and username[0].isupper():
            return username
        raise ValidationError('Имя не корректное!')

    def clean_password_2(self):
        pass1 = self.cleaned_data.get('password_1')
        pass2 = self.cleaned_data.get('password_2')
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError('Пароли не совпадают либо не заполнены')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_1'])
        if commit:
            user.save()
        return user

