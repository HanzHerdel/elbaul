from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Galeria, rating
import random
#from django.shortcuts import get_object_or_404
#variablequerry=get_object_or_404(var,pk=variable_id)
# Create your views here.

		#if request.method == 'POST':
		#	print 'asdfasdfasdgasfdgasdgfas///////'
#def get_img():
#	n= len(galeria)-1
#	n = random.randint(0,n)
#	imagenes = galeria[n].imagenes.all()
#	return imagenes
class index(View):
	def post(self, request, **kwargs):
		rate = rating.objects.create(nombre=request.POST['nombre'],
			email=request.POST['mail'],rating=request.POST['rating'],
			comment=request.POST['comment'])
		rate.save()
		return redirect('/')
	def get(self, request,*args,**kwargs):
		#seleccion aleatoria de galeria y  captacion de sus imagenes
		galerias = []
		galeria = Galeria.objects.all()
		m=0
		n= len(galeria)-1
		n = random.randint(0,n)
		imagenes = galeria[n].imagenes.all()
		#acumulacion de galerias y sus respectivas imagenes/descripciones
		for gal in galeria:
			gal= {'imagenes':gal.imagenes.all(),'descripcion':gal.descripcion, 'nombre':gal.nombre}
			m=m+1
			galerias.append(gal)
		feedback= rating.objects.all()
		return render(request, "base.html",{'galeria':imagenes,'galerias':galerias,'feedback':feedback,
			'lengal':len(imagenes),'urls':["about.html","activities.html","contact.html",
			"gallery.html","program.html","rating.html","staff.html","volunteer.html"]})



