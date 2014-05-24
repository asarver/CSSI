# picture editing pages

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class MyUser(users.User):
    def __init__(self, name): self.name = name
    def nickname(self): return self.name


def get_user(page):
    user = users.get_current_user() # used for online use
    # user = users.User("hi@test.com") # only used for local server
    if user: return user
    page.redirect(users.create_login_url(page.request.uri))
    return None



# -----------------------------------------------------------------
# WEB PAGE DEFINITIONS

class MainPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        self.response.out.write("""
<html>
<body>
Hola, %s

</body>
</html>

""" % user.nickname() )



application = webapp.WSGIApplication(
    [("/", MainPage)], debug = True)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
