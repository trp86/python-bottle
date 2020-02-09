from bottle import route,run,install,template,request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile=r'/home/trp86/python-bottle/database/inventory.db')) 

@route('/show/<devicename>')
def show_device(db,devicename):
	command=db.execute('SELECT id,name,os from devices where name = ?',(devicename,))
	row=command.fetchone() or None
	if row:
		return template('{{id}},{{name}},{{os}}',id=row['id'],name=row['name'],os=row['os'])
	else:
		return template('The specified device with name :{{name}},couldnot be found!',name=devicename)	

@route('/show')
def querylike(db):
	os=request.query.os or None
	id=request.query.id	or None
	name=request.query.name or None

	print(os)
	print(id)
	print(name)
	

	querystring=[]

	if os:
		querystring.append("os like '{}'".format(os))

	if id:
		querystring.append('id={}'.format(id))

	if name:
		querystring.append("name like '{}'".format(name))

	if len(querystring) == 0:
		return 'Invalid Query!'
	else:
		print(querystring)
		query='SELECT id,name,os from devices where {}'.format(' AND '.join(querystring))
		print(query)
		command=db.execute(query)
		row=command.fetchone() or None
		
		if row:
			return template('{{id}},{{name}},{{os}}',id=row['id'],name=row['name'],os=row['os'])
		else:
			return template('The specified device with name :{{name}},couldnot be found!',name=name)	
			

	
run(host="localhost",port=8082,debug=True)		