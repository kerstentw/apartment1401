import web, engine

urls = (
"/index","INDEX"
)

app = web.application(urls, globals())
render = web.template.render("templates/")

class INDEX(object):

	def __init__(self):
		self.engine_instance = engine.Engine()

	def GET(self):
		content = self.engine_instance.startRoom()
		return render.index(content = content)
		
	def POST(self):
		
		try:
			choice = web.input()
			next_choice = choice.content1 #content1 is the name of the set of radio buttons on the format
			content = self.engine_instance.nextRoom(next_choice)
			return render.index(content = content)
		
		except:
			content = 'Racked with indecision, you ponder for a bit. PRESS BACK!'
			return render.index(content = content)
			
if __name__ == "__main__":
	app.run()