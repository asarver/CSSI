# myapp.py

import chart

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app

class MyUser(users.User):
    def __init__(self, name): self.name = name
    def nickname(self): return self.name

def get_user(page):
    """return a user or non and a do a redirect"""
    # user = users.User("asarver1@gmail.com")
    user = users.get_current_user()
    if user: return user
    page.redirect(users.create_login_url(page.request.uri))
    return None

def count_votes(votes):
    """return dictionary with number of votes per celebrity"""
    diction = {}
    for vote in votes:
        if not vote.celebrity:
            pass
        elif vote.celebrity in diction:
            diction[vote.celebrity] = diction[vote.celebrity] + 1
        else:
            diction[vote.celebrity] = 1
    return diction
        

# ---------------------------------------------------------------
# DATASTORE OBJECTS

class CelebrityVote(db.Model):
    user = db.UserProperty()
    celebrity = db.StringProperty()
    data = db.DateTimeProperty(auto_now_add = True)

def add_vote(user, celebrity):
    vote = CelebrityVote()
    vote.user = user
    vote.celebrity = celebrity
    vote.put()
    
def get_votes():
    votes = db.GqlQuery("SELECT * FROM CelebrityVote")
    return votes
    
# ---------------------------------------------------------------
# WEB PAGE DEFINITIONS



class MainPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        self.response.out.write("""

<html>
<body>
<img src = "/artwork/google.pmg" />
<h1>My Awesome Website</h1>

Hello <b>%s</b>!
<p />
Take my <a href = "/quiz">quiz</a>!
Or see the <a href = "/results">votes</a>.
</body>
</html>
""" % user.nickname())
        


class QuizPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        self.response.out.write("""
<html>
<body>

<head>
<title>
My Awesome Quiz
</title>
</head>

<form action = "/answer" method = post>
Who is your favorite celebrity?<p />
<input type = radio name = "celebrity" value = "Justin Bieber" />
Justin Bieber<br />
<input type = radio name = "celebrity" value = "Lady Gaga" />
Lady Gaga<br />
<input type = radio name = "celebrity" value = "Guido Rossum" />
Guido Rossum<p />
<input type = submit value = "answer" />
</form>
</body>
</html>""")


class AnswerPage(webapp.RequestHandler):
    def post(self):
        user = get_user(self)
        if not user: return
        celebrity = self.request.get("celebrity")
        # store user's vote
        add_vote(user, celebrity)
        self.response.out.write("""
<html>
<body>
You chose <b>%s</b>.
See all the <a href = "/results">results</a>.
</body>
</html>""" % celebrity)


class ResultsPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        votes = get_votes()
        diction = count_votes(votes)
        if not diction:
            self.response.out.write("No votes!")
            return
        charturl = chart.dictionary_chart(diction)
        self.response.out.write("""

<html>
<body>
Here are the votes:
<p />
<img src = "%s" />
</body>
</html>

""" % charturl)

class BeatlesPage(webapp.RequestHandler):
    def get(self):
        user = get_user(self)
        if not user: return
        self.response.out.write(
            "hello, goodbye\n" + "I am the walrus")



application = webapp.WSGIApplication(
    [("/", MainPage), ("/beatles", BeatlesPage), ("/quiz", QuizPage),
     ("/answer", AnswerPage), ("/results", ResultsPage)],
    debug = True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()


