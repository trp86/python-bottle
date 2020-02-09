from bottle import route,run,template,request

# wikipage?pageid=108&section=b
@route('/wikipage')
def wiki_page():
	pageid=request.query.pageid or '1'
	section=request.query.section or 'a'
	return template("The requested wike page page id {{pageid}} and section is {{section}}",pageid=pageid,section=section)

run(host="localhost",port=8082,debug=True)		