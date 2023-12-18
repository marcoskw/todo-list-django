from django import forms
from .models import List


class TodoListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = (
            'title',
        )
        exclude = (
            'status',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
