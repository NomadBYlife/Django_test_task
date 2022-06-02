from django import forms


class FormForID(forms.Form):
    """Форма для принятия ID контракта"""
    id = forms.IntegerField(label='ID контракта')
