from django.contrib import admin
# Register your models here.
from .models import Galeria
from .models import imagenDeGaleria
from .models import rating

admin.site.register(Galeria)
admin.site.register(imagenDeGaleria)
admin.site.register(rating)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
def image_tag(self):
	return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.imagen))
image_tag.short_description = 'Image'