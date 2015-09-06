# Create your views here.
from blog.models import Entrada
from django.http import HttpResponse
# home
from django.shortcuts import render_to_response
#  
from django.shortcuts import render




def prueba(request):
 	verentradas = Entrada.objects.all().order_by('-fecha')[:5]
	output = ','.join([p.titulo for p in verentradas])
	return HttpResponse(output)


def home(request):
    return render_to_response('home.html')

def metodo2(request):
	Entrada_list = Entrada.objects.all().order_by('-fecha')[:5]
	context = {'object_list': Entrada_list}
	# context = ','.join([p.titulo for p in Entrada_list])
	return render(request, 'home.html', context)