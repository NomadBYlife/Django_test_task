from django import forms


class FormForID(forms.Form):
    id = forms.IntegerField(label='ID контракта')
