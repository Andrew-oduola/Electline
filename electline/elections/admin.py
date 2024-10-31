from django.contrib import admin
from .models import Election, Vote, Candidate

# Register your models here.
@admin.decorators.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'allowed_prefix']
    list_filter = ['start_date', 'end_date']
    search_fields = ['title', 'allowed_prefix']
    list_editable = ['allowed_prefix']
    ordering = ['start_date']
    prepopulated_fields = {'slug': ['title']}


@admin.decorators.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'election', 'candidate']
    list_filter = ['election__start_date', 'election__end_date']
    search_fields = ['user', 'election__title']


@admin.decorators.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'election']
    list_filter = ['election']
    raw_id_fields = ['election']
    ordering = ['name']

