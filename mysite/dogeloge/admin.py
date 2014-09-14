from django.contrib import admin
from .models import DogWalker
from .models import DogOwner

@admin.register(DogWalker)
class DogWalkerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'company_name', 'phone_number',
              'email']

@admin.register(DogOwner)
class DogOwnerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'phone_number', 'email',
              'emergency_contact', 'contact_phone', 'vet_name', 'vet_phone',
              'dogwalker']
