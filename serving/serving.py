from bottle import static_file,route,run

@route('/show/<file>')
def show(file):
	return static_file(file,root=r'/home/trp86/python-bottle/serving/')

@route('/download/<file>')
def download(file):
	return static_file(file,root=r'/home/trp86/python-bottle/serving/',download=file)

run(host="localhost",port=8082,debug=True)