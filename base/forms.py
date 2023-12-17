from django import forms
from .models import Attendee, Event

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['ticket']

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        event_id = kwargs.pop('event_id', None)
        if event_id:
            self.fields['ticket'].queryset = self.fields['ticket'].queryset.filter(event__id=event_id)

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields  = ['title', 'description', 'date', 'location', 'organizer', 'category', 'image']
