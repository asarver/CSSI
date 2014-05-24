# helloworld.py

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

class MainPage(webapp.RequestHandler):
	def get(self):
		g_user = users.get_current_user()
		if not g_user:
			self.redirect(users.create_login_url(self.request.uri))
		user = logic.get_player(users.get_current_user())
		#user = logic.get_player(users.User("johncena4president@gmail.com"))
		if logic.get_game_for_user(user.user_id):
			game = logic.get_game_for_user(user.user_id)
		else:
			game = logic.make_game(user)
		
		# ---- These should really live in logic.make_game() but being able to comment then out here is so convinent ----
		#logic.draw_dealer_card(game.game_id)
		#logic.draw_player_card(game.game_id)
		
		moves = database.get_moves(game.game_id)[0]
		
		dealer_value = logic.get_hand_value(moves.dealer_cards)
			
		template_values = ({ 'dealer_cards': moves.dealer_cards, 'dealer_value': dealer_value, 'player_cards': moves.cards_one,
							'player_cash': user.cash, 'game_id': game.game_id, 'user_id': user.user_id })
		path = os.path.join(os.path.dirname(__file__), 'game.html')
		self.response.out.write(template.render(path, template_values))
		
class PlayPage(webapp.RequestHandler):
	def post(self):
		action = self.request.get("action")
		game_id = self.request.get("game_id")
		user_id = self.request.get("user_id")
		bet_amount = self.request.get("bet_amount")
				
		if action == "Hit":
			logic.hit_logic(self, game_id, user_id, bet_amount)
		elif action == "Stay":
			logic.stay_logic(self, game_id, user_id, bet_amount)

class BustPage(webapp.RequestHandler):
	def get(self):
		cash = self.request.get("n")
		self.response.out.write("""
		<html>
<head>
<link href="../stylesheets/iframes.css" rel="stylesheet" type="text/css">
</head>
<body style="text-align:center; margin: auto;">
<p>You busted!</p>
<p>Your new cash total is: %s</p>
<p><a href="../game/">Play again?</a></p>
</body>
</html>""" % cash)

class LosePage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""<html>
		<head>
<link href="../stylesheets/iframes.css" rel="stylesheet" type="text/css">
</head>
<body style="text-align:center; margin: auto;">
<p>You lose!</p>
<p><a href="../game/">Play again?</a></p>
</body>
</html>""")
	
class WinPage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""<html>
		<head>
<link href="../stylesheets/iframes.css" rel="stylesheet" type="text/css">
</head>
<body style="text-align:center; margin: auto;">
<p>You win!</p>
<p><a href="../game/">Play again?</a></p>
</body>
</html>""")
		
application = webapp.WSGIApplication(
                                    [("/game/", MainPage), ("/game/play", PlayPage), ("/game/bust", BustPage), ("/game/win", WinPage),
									("/game/lose", LosePage)], debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

		
