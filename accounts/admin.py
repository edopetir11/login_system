from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserAccount, Divisi, Jabatan

admin.site.register(UserAccount)
admin.site.register(Divisi)
admin.site.register(Jabatan)

admin.site.unregister(Group)
