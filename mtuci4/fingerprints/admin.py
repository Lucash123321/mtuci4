from django.contrib import admin
from django.db import models
from fingerprints.models import Fingerprint

# Register your models here.
@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    pass