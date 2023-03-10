from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
import re
from webapp.models.projects import Project


def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError("Максимальная длина строки 20 символов")
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20):
        message = 'максимальное значение %(limit_value) Вы ввели %(show_value)'
        super(CustomLengthValidator, self).__init__(limit_value, message=message)

    def compare(self, value, limit_vale):
        print(value)

    def clean(self, value):
        return len(value)


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=123,
        validators=(MinLengthValidator(limit_value=2, message='Малая длина'),
                    CustomLengthValidator(limit_value=10),
                    max_length_validator)
                    )

    class Meta:
        model = Project
        fields = ('title', 'description', 'task')


    def clean_title(self):
        title = self.cleaned_data.get('title')

        if re.match(r'\d', title):
            raise ValidationError('Не должно начинаться с цифры')

        if Project.objects.filter(title=title).exists():
            raise ValidationError('Запись с таким заголовком уже существует')

        return title

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")
