# forms.py

from django import forms
from .models import Attendee

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['ticket']

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        # Customize the form if needed, for example, you can limit ticket choices to available tickets for the event
        event_id = kwargs.pop('event_id', None)
        if event_id:
            self.fields['ticket'].queryset = self.fields['ticket'].queryset.filter(event__id=event_id)

    # You can add custom validation or override save() method if needed
