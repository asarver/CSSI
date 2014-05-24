#
#  blackjack_database.py
#  
#
#

from google.appengine.ext import db
from google.appengine.api import users

# ------- DATASTORE FUNCTIONS --------------
# 
class Game(db.Model):
    users = db.UserProperty()
    game_id = db.StringProperty()
	
class OldGames(db.Model):
	users = db.UserProperty()
	game_id = db.StringProperty()
	winner = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now_add = True)

class User(db.Model):
	user_id = db.IntegerProperty()
	user = db.UserProperty()
	cash = db.IntegerProperty()
	current_games = db.ListProperty(str)

class Moves(db.Model):
	game_id = db.StringProperty()
	# list of what cards have been played already, needed by the random card generator to be fair
	deck_one = db.ListProperty(str)
	deck_two = db.ListProperty(str)
	# list of cards the players and dealer currently have on the board
	cards_one = db.ListProperty(str)
	cards_two = db.ListProperty(str)
	dealer_cards = db.ListProperty(str)
	
def get_games():
	games = db.GqlQuery("SELECT * From Game")
	return games

#def get_game_for_user(user):
	#games = get_games()
	#for game in games:
	#	if user in games.users:
	#		return game
	#return None

def get_users():
	users = db.GqlQuery("SELECT * From User")
	return users
	
def get_user_by_id(user_id):
	user = db.GqlQuery("SELECT * From User where user_id = "+str(user_id))
	return user[0]

def get_moves(id):
	moves = db.GqlQuery("Select * FROM Moves WHERE game_id = :1", id)
	return moves
	
def get_game(id):
	game = db.GqlQuery("SELECT * FROM Game WHERE game_id = :1", id)
	return game[0]