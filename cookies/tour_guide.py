from bottle import run,route,response,request,redirect

@route('/',method=['GET','POST'])
def index():
	if request.method == 'GET':
		return '''<form action="/" method="post" enctype="multipart/form-data">
						Username:<input type="text" name="username" /> 
						Password:<input type="password" name='password'>
								<input type="submit" value="Login" /> 
				   </form> '''
	else:
		if request.forms.get('username') == 'admin' and request.forms.get('password') == 'pass':
			response.delete_cookie('simple')
			response.delete_cookie('guest')
			response.set_cookie('admin','yes')
			return redirect('/welcome')
		elif request.forms.get('user') == 'user' and request.forms.get('password') == 'nothing':
			response.delete_cookie('admin')
			response.delete_cookie('guest')
			response.set_cookie('simple','yes')
			return redirect('/welcome')

		response.delete_cookie('admin')
		response.delete_cookie('simple')	
		response.set_cookie('guest','yes')	
		return redirect('/welcome')			   

@route('/welcome')
def welcome():
	if request.get_cookie('admin'):
		return "Welcome back administrator!"
	elif request.get_cookie('simple'):
		return "You are just an average user!"
	else:
		return "Welcome guest.You have limited functionality!"	

run(host='localhost',port=8080,debug=True)	
