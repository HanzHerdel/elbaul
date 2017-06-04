from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Galeria(models.Model):
    nombre = models.TextField(max_length = 30)
    descripcion = models.TextField(default="Baul's Images!", max_length = 123)
    def __str__(self):
    	return self.nombre

class imagenDeGaleria(models.Model):
    galeria = models.ForeignKey(Galeria, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes/%Y%m%d/')
    def __str__(self):
    	return self.imagen.url

class rating(models.Model):
	rating= models.DecimalField(max_digits=3, decimal_places=2)
	nombre= models.CharField(max_length = 60)
	email= models.CharField(max_length = 60, blank=True)
	comment = models.TextField(max_length = 1000)
	posted_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.nombre