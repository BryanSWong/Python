import web

urls = (
	'/upload', 'Upload'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Upload:
	def GET(self):
		return render.upload()

	def POST(self):
		x = web.input(myfile={})
		# change this to the directory you want to store the file in.
		filedir = '/home/msb/projects/ex51/uploads'
		fout = open(filedir +'/'+ x['myfile'].name + '.jpg','w')
		# writes the uploaded file to the newly created file.
		fout.write(x.myfile.file.read())
		# closes the file, upload complete.
		fout.close()
		raise web.seeother('/upload')

if __name__ == "__main__":
	app.run()