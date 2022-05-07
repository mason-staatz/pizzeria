from django import forms

from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]
        labels = {"comment": ""}
        widgets = {"comment": forms.Textarea(attrs={"cols": 30})}