from django.contrib import admin
from PollApp.models import Poll, Choice, Vote
# Register your models here.

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
