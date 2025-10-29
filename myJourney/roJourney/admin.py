from django.contrib import admin
from .models import Profile, LearningEntry

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'student_id', 'email', 'created_at')
    search_fields = ('full_name', 'student_id')

@admin.register(LearningEntry)
class LearningEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'content')

