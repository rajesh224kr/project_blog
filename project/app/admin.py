from django.contrib import admin
from app.models import Images

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    class Meata:
        model   = Images
        fields  = '__all__'
        list_display    =["name","location",'image']

admin.site.register(Images,ImageAdmin)