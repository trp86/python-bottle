from bottle import route,run


@route('/')
def index():
	return 'WELCOME !!!!!'

@route('/anotherexampleroute')
def index():
	return 'WELCOME TO ANOTHER EXAMPLE ROUTE!!!!!'	

run(host="localhost",reloader=True,	port=8082,debug=True)		