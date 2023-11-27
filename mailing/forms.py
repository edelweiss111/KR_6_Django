from django import forms

from mailing.models import Client, Message, Mailing


class StyleFormMixin:
    """Миксин для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Client"""

    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Message"""

    class Meta:
        model = Message
        fields = '__all__'


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Mailing"""

    class Meta:
        model = Mailing
        exclude = ('status',)
        widgets = {
            'time':  forms.TimeInput(
                attrs={'type': 'time', }
            ),
            'date': forms.DateInput(
                attrs={'type': 'date', }
            )
        }
