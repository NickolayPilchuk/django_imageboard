from django.contrib import admin
from .models import Threads,Comments,Status
# Register your models here.
admin.site.register(Threads)
admin.site.register(Comments)
admin.site.register(Status)