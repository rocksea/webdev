from django.http import HttpResponse
# Create your views here.
def main_page(request):
	output ='''
		<html>
		<head><title>%s</title></head>
		<body>
			<h1>%s</h1>
			<p>%s</p>
		</body>
		</html>
		''' % ( 'Django TEST',
			'Welcome to Django',
			'Hello World!!'
		)
	return HttpResponse(output)
