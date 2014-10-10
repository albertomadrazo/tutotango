from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world!")

def follatela(request):
	da_loop = 0
	for i in range(4):
		da_loop += i * 9 - 17

	return HttpResponse(da_loop)