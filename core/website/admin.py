from django.contrib import admin
from website.models import ContactForm

# Contact admin panel
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_date")
    list_filter = ("email", "subject")
    search_fields = ("email", "subject")
    ordering = ("-created_date",)
    
    
admin.site.register(ContactForm, ContactAdmin)
