from django.contrib import admin
from img.models import Image

# Register your models here.
admin.site.register(Image)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['Id','photo','upload_date']