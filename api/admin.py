from django.contrib import admin
from .models import User, Qa, Group, Data
# Register your models here.
admin.site.register(User)
admin.site.register(Qa)
admin.site.register(Group)
admin.site.register(Data)