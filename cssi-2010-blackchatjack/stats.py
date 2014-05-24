#
#  stats.py
#  
#
#  Created by Kasra Rahjerdi on 8/12/10.
#  Copyright (c) 2010 __MyCompanyName__. All rights reserved.
#

from google.appengine.api.images import Image
from google.appengine.api import xmpp
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os
import uuid
import random
import blackjack_logic as logic
import blackjack_database as database

class GameProperty(object):
	def __init__(self, user, winner):
		self.user = user
		self.winner = winner
		self.dealer_won = False
		if winner == "dealer":
			self.dealer_won = True

class MainPage(webapp.RequestHandler):
	def get(self):
		oldgames = db.GqlQuery("SELECT * FROM OldGames order by timestamp desc")
		games = []
		
		for g in oldgames:
			g.append(GameProperty(g.users, gu.winner))
			
		template_values = { 'games': games }
				
		path = os.path.join(os.path.dirname(__file__), 'stats.html')
		self.response.out.write(template.render(path, template_values))
		
application = webapp.WSGIApplication(
                                    [("/stats/", MainPage)])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

