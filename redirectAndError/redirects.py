from bottle import route,run,redirect

@route('/')
def index():
	return 'Please authorize yourself!'

@route('/restricted')
def restricted():
	#authorization function
	#if it fails
	redirect('/')


run(host="localhost",port=8080,debug=True)	