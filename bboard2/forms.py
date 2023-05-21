from django import forms
from .models import Defense, Grade


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('commission', 'student', 'value', 'question')

    def __init__(self, *args, **kwargs):
        commission_choices = kwargs.pop('commission_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['commission'].choices = commission_choices

class DefenseForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    COMMENT_CHOICES = [
        ('Выберите', ' '),
        ('Отлично', 'Отлично'),
        ('Хорошо', 'Хорошо'),
        ('Удовлетворительно', 'Удовлетворительно'),
    ]
    comment = forms.ChoiceField(choices=COMMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Defense
        fields = ['start_time', 'end_time', 'comment']

class CharacteristicForm(forms.ModelForm):
    COMMENT_CHOICES = [
        ('Выберите', ' '),
        ('Уверенно', 'отвечал уверенно и правильно'),
        ('бирнарсе', 'бирнарсе'),
        ('екинарсе', 'екинарсе'),
    ]
    comment = forms.ChoiceField(choices=COMMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Defense
        fields = ['comment']