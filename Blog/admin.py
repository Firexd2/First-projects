from django.contrib import admin
from Blog import models

admin.site.register(models.Post)

admin.site.register(models.Image)

admin.site.register(models.InformationsClient)