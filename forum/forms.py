from django import forms
from django.utils.translation import gettext as _
from forum.models import Topic
from forum.models import Message

class NewTopicForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': _("A quoi pensez vous ?")}
        ),
        max_length=4000,
        help_text = _("Le nombre de caractères minimum est de 4000.")
    )

    class Meta:
        model = Topic
        fields = ['subject', 'text']


class ReplyMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text',)
