#main.py
# the import section
import webapp2
import os
import jinja2

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        index_template = jinja_current_dir.get_template("templates/index.html")
        self.response.write(index_template.render())

class ReportPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello yourself, bub!') #the response
# the app configuration section
class FindPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello yourself, bub!') #the response
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/findfood',FindPage),
    ('/reportfood',ReportPage)
], debug=True)
