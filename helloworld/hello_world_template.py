from bottle import route,run,template

@route('/')
def index():
	return template('Welcome to bottle {{name}} !',name="Stranger")

run(host="localhost",port=8080,debug=True)	