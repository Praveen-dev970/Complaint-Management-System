from django.contrib import admin

# Register your models here.
from .models import Complaint, Profile, Grievance

admin.site.register(Complaint)
admin.site.register(Profile)
admin.site.register(Grievance)
