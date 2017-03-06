from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	page = """
	<html>
	<body>
	Bribes management application
	</body>
	</html>
	"""
	return HttpResponse(page)