from django.contrib import admin
from .models import Event, Ticket, Attendee, Notification, UserProfile, Category

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'price', 'quantity_available')

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'event', 'ticket', 'registration_date')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'location')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

   

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
