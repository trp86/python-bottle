from bottle import route,run,template

@route('/')
def index():
	return "Welcome to bottle stranger!"

run(host="localhost",port=8080,debug=True)	