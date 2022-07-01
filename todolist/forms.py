from django import forms
from django.forms import widgets
from todolist.models import STATUS_CODE


class TaskForm(forms.Form):
    task = forms.CharField(max_length=50, required=True, label="Task")
    description = forms.CharField(max_length=2000, required=True, label="Description",
                                  widget=widgets.Textarea(attrs={"cols": 30, "rows": 2}))
    status = forms.ChoiceField(choices=STATUS_CODE, label="Status")
    created_at = forms.DateField(label="Date")
