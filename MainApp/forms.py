from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code']
        labels = {'name': 'Название', 'lang': 'Язык прграммирования', 'code': 'Пример кода на языке',}
        widgets = {
                  'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
                  'code': Textarea(attrs={'placeholder': 'Код сниппета'}),
        }