import web, engine

urls = (
"/index","INDEX"
)

app = web.application(urls, globals())
render = web.template.render("templates/")

class INDEX(object):

	def GET(self):
		content = engine.gamerun()
		return render.index(content = content)
		
	def POST(self):
		pass
		
if __name__ == "__main__":
	app.run()