from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event, Ticket, Attendee, Category
from .forms import EventRegistrationForm, EventCreationForm

def home(request):
    return render(request, 'base/home.html')

def event_list(request):
    events = Event.objects.all()
    categories = Category.objects.all()

    context = {
        'events': events,
        'categories': categories,

    }
    return render(request, 'base/event_list.html', context)

#def category_detail(request, catego)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    tickets = Ticket.objects.filter(event=event)
    return render(request, 'base/event_detail.html', {'event': event, 'tickets': tickets})

@login_required
def event_registration(request, pk, category_slug=None):
    event = get_object_or_404(Event, pk=pk)
    ticket_id = request.POST.get('ticket_id')
    categories = Category.objects.all()


    if category_slug:
        category = Category.objects.get(slug=category_slug)
        events = events.filter(category=category)

    if ticket_id:
        ticket = get_object_or_404(Ticket, pk=ticket_id)

        if ticket.quantity_available > 0:
            attendee, created = Attendee.objects.get_or_create(
                user_profile=request.user.userprofile,
                event=event,
                ticket=ticket
            )

            if created:
                ticket.quantity_available -= 1
                ticket.save()
                messages.success(request, f"You have successfully registered for {event.title}.")
            else:
                messages.warning(request, f"You are already registered for {event.title}.")
        else:
            messages.error(request, f"Sorry, no more tickets available for {event.title}.")

    return redirect('event_list')

@login_required
def user_dashboard(request):
    user_profile = request.user.userprofile
    events_attending = user_profile.events_attending.all()
    notifications = user_profile.notifications.all()

    # Assuming you have a user_event_data DataFrame with user-event interactions
    user_event_data = get_user_event_data(request.user.id)

    # Initialize the EventRecommender with user-event interactions
    recommender = EventRecommender(user_event_data)

    # Get recommended event IDs for the current user
    recommended_events = recommender.recommend_events(request.user.id, num_recommendations=5)

    # Fetch recommended events from the database
    recommended_events_data = Event.objects.filter(pk__in=[event_id for event_id, _ in recommended_events])

    context = {
        'events_attending': events_attending,
        'notifications': notifications,
        'recommended_events': recommended_events_data,
    }

    return render(request, 'base/user_dashboard.html', context)

@login_required
def event_registration(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        form = EventRegistrationForm(request.POST, event_id=pk)

        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.user_profile = request.user.userprofile
            attendee.event = event

            if attendee.ticket.quantity_available > 0:
                attendee.ticket.quantity_available -= 1
                attendee.ticket.save()
                attendee.save()
                messages.success(request, f"You have successfully registered for {event.title}.")
            else:
                messages.error(request, f"Sorry, no more tickets available for {event.title}.")

            return redirect('event_list')
    else:
        form = EventRegistrationForm(event_id=pk)

    return render(request, 'base/event_registration.html', {'form': form, 'event': event})

def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)

        if form.is_valid():
            event = form.save()
            print("Event created successfully:", event)
            return redirect('event_list')
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
    else:
        form = EventCreationForm()
    context = {
        'form':form,

    }
    return render(request, 'base/event_creation.html', context)

def update_event(request,  slug):
    #event =  get_object_or_404(Event, )
    events = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        form = EventCreationForm(request.POST, instance=events)

        if form.is_valid():
            event = form.save()
            print("Updated Successfully")

            return redirect('event_list')
        else:
            print("There was an error")

    else:
    
        form  = EventCreationForm(instance=events)
    context = {
        'form':form,
        'events':events,
    }
    return render(request, 'base/update_event.html', context)

def delete_event(request, slug):

    event = get_object_or_404(Event, slug=slug)

    if request.method == 'POST':
        event.delete()

        return redirect('event_list')

    context = {

        'event':event,
    }
    return render(request, 'base/delete_event.html', context)