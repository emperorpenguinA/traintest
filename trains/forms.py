from django import forms
from .models import Item


class ItemForm(forms.ModelForm):


    class Meta:
        model = Item
        fields = ('name', 'route', 'thumnail','memo')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'記入例: 山田　太郎'}),
            'route': forms.CheckboxSelectMultiple(),
            'thumnail': forms.FileInput(),
            'memo': forms.Textarea(attrs={'rows':4}),
        }