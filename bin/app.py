import web, engine

urls = (
"/index","INDEX"
)

app = web.application(urls, globals())
render = web.template.render("templates/")

class INDEX(object):

	def GET(self):
		content = 'You are on the title screen!  What next?\
		<form type = "input" action = "/" method = "post"><br/>\
			<input type = "radio" name = "start" value = "choice1">Name</input>\
		</form>'
		return render.index(content = content)
		
	def POST(self):
		pass
		
if __name__ == "__main__":
	app.run()