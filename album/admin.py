from django.contrib import admin
from .models import registro

@admin.register(registro)
class registroAdmin(admin.ModelAdmin):
		pass