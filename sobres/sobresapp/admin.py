from django.contrib import admin

# Register your models here.
from sobresapp.models import Donor, Sobre

admin.site.register(Donor)
admin.site.register(Sobre)