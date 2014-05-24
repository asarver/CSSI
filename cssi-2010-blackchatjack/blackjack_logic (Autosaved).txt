#
#  blackjack_logic.py
#  
#
#

from google.appengine.ext import db
from google.appengine.api import users
import random
import uuid
import urllib
import blackjack_database as database

basepath = "../images/"

suffixes_list = ["ace/","two/","three/","four/","five/","six/","seven/","eight/",
            "nine/", "ten/", "jack/", "queen/", "king/"]

suit_list = ["diamonds","clubs","spades","hearts"]

back_location = '../images/back.png'

def get_card(deck_one, deck_two):
	num = random.randint(0,11)
	path = basepath+suffixes_list[num]
	suit = suit_list[random.randint(0,3)]
	path += suit+".png"

	if path not in deck_one:
		deck_one.append(path)
		return ('<img src="%s" />' % path, deck_one, deck_two)
	elif path not in deck_two:
		deck_two.append(path)
		return ('<img src="%s" />' % path, deck_one, deck_two)
	else:
		return get_card(deck_one, deck_two)

num_list = { "ace": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10 }

def get_hand_value(cards):
	hand_value = 0
	aces = 0
	for c in cards:
		if "back" not in c:
			card = c.split("/")[2]
			if card == "ace":
				aces += 1
			else:
				hand_value += num_list[card]
	for x in range(aces):
		if hand_value + 11 > 21:
			hand_value += 1
		else:
			hand_value += 11
	return hand_value

def end_game(game_id, user_id):
	game = database.get_game(game_id)
	moves = database.get_moves(game_id)[0]
	dealer_value = get_hand_value(moves.dealer_cards)
	user_one = get_hand_value(moves.cards_one)
	#user_two = get_hand_value(game.cards_two)
	user_two = 0
	
	oldGame = database.OldGames()
	oldGame.users = game.users
	oldGame.game_id = game_id
	if dealer_value > user_two and dealer_value < 21 :
		oldGame.winner = "dealer"
	else:
		oldGame.winner = "player"
	oldGame.put()
		
	user = database.get_user_by_id(user_id)
	user.current_games.remove(game_id)
	user.put()
	
	game.delete()
		
	# TODO:
	# TURN this game into an oldgame data structure
	
	#if dealer_value > user_one and dealer_value > user_two:
	#	return "The house wins!"
	#elif user_one > user_two and user_one > dealer_value:
	#	return "User one wins!"
	#elif user_two > user_one and user_two > dealer_value:
	#	return "User two wins!"

	
def draw_dealer_card(game_id):
	moves = database.get_moves(game_id)[0]
	deck_one = moves.deck_one
	deck_two = moves.deck_two
	
	card, d_one, d_two = get_card(deck_one, deck_two)
	
	if '<img src="'+back_location+'" />' in moves.dealer_cards:
		moves.dealer_cards[moves.dealer_cards.index('<img src="'+back_location+'" />')] = card
	else:
		moves.dealer_cards.append(card)
	moves.deck_one = d_one
	moves.deck_two = d_two
	moves.put()
	
	return card
	
def draw_hidden_dealer_card(game_id):
	moves = database.get_moves(game_id)[0]
	deck_one = moves.deck_one
	deck_two = moves.deck_two
	
	#card, d_one, d_two = get_card(deck_one, deck_two)
	game = db.GqlQuery("SELECT * FROM Game WHERE game_id = :1",game_id)
	
	card = '<img src="'+back_location+'" />'
	
	moves.dealer_cards.append(card)
	moves.put()
	
	return card
	
def draw_player_card(game_id, user):
	moves = database.get_moves(game_id)[0]
	deck_one = moves.deck_one
	deck_two = moves.deck_two
	
	card, d_one, d_two = get_card(deck_one, deck_two)
	
	game = db.GqlQuery("SELECT * FROM Game WHERE game_id = :1",game_id)[0]
	
	moves.cards_one.append(card)
	
	moves.deck_one = d_one
	moves.deck_two = d_two
	moves.put()
	
	return card

def make_player(user):
	count = database.get_users().count()
	this_user = database.User()
	this_user.user_id = count
	this_user.user = user
	this_user.cash = 2500
	this_user.current_games = []
	this_user.put()
	
	return this_user

def get_player(user):
	this_user = db.GqlQuery("SELECT * From User where user = :1",user)
	if this_user.count() == 0:
		return make_player(user)
	else:
		return this_user[0]
	
def make_game(user_one):
	id = uuid.uuid1().hex
	
	#user_two = make_player(users.User("admin@celsior.org"))
	
	u_one = user_one.user
	#u_two = user_two.user
	this_game = database.Game()
	this_game.users = u_one
	this_game.game_id = id
	this_game.put()
	
	# Let's add this game id to both the user's current_games list
	#print user_one_id
	user_one.current_games.append(id)
	user_one.put()
	#user_two.current_games.append(id)
	#user_two.put()
	
	# So we created a game, let's get use its ID to create a blank Moves database for this game
	these_moves = database.Moves()
	these_moves.game_id = id
	these_moves.put()
	
	draw_dealer_card(id)
	draw_hidden_dealer_card(id)
	draw_player_card(id, user_one)
	draw_player_card(id, user_one)
	
	return this_game

def count_user_games(user_id):
	games = db.GqlQuery("SELECT * FROM User where user_id = :1", user_id)
	return games.count()

def get_game_for_user(user_id):
	user = db.GqlQuery("SELECT * FROM User where user_id = :1", user_id)[0]
	if len(user.current_games) > 0:
		game_id = user.current_games[len(user.current_games)-1]
		return database.get_game(game_id)
	else:
		return None

def did_player_bust(game_id, user_id):
	game = database.get_game(game_id)
	moves = database.get_moves(game_id)[0]
	
	this_user = database.get_user_by_id(user_id).user
	if get_hand_value(moves.cards_one) > 21:
			return True
	return False
		
def should_dealer_draw(game_id):
	moves = database.get_moves(game_id)[0]
	
	if get_hand_value(moves.dealer_cards) < 16:
		return True
	else:
		return False

def did_dealer_bust(game_id):
	moves = database.get_moves(game_id)[0]
	
	if get_hand_value(moves.dealer_cards) > 21:
		return True
	else:
		return False
	
def hit_logic(page, game_id, user_id, bet_amount):
	game = db.GqlQuery("SELECT * FROM Game WHERE game_id = :1", game_id)[0]
	#print page.request
	this_user = db.GqlQuery("SELECT * From User WHERE user_id = "+str(user_id))[0]
	
	draw_player_card(game_id, this_user.user)
	
	if did_player_bust(game_id, user_id):
		this_user.cash -= long(bet_amount)
		this_user.put()
		end_game(game_id, user_id)
		page.redirect("/game/bust?n="+str(this_user.cash))
	elif should_dealer_draw(game_id):
		draw_dealer_card(game_id)
		if did_dealer_bust(game_id):
			end_game(game_id, user_id)
			this_user.cash += long(bet_amount)
			this_user.put()
			page.redirect("/game/win")
		else:
			page.redirect("/game/")
	else:
		page.redirect("/game/")

def stay_logic(page, game_id, user_id, bet_amount):
	game = db.GqlQuery("SELECT * FROM Game WHERE game_id = :1", game_id)[0]
	#print page.request
	this_user = db.GqlQuery("SELECT * From User WHERE user_id = "+str(user_id))[0]
	moves = database.get_moves(game_id)[0]
	
	if should_dealer_draw(game_id):
		draw_dealer_card(game_id)
		if did_dealer_bust(game_id):
			end_game(game_id, user_id)
			this_user.cash += long(bet_amount)
			this_user.put()
			page.redirect("/game/win")
		else:
			page.redirect("/game/")
	else:
		if get_hand_value(moves.dealer_cards) > get_hand_value(moves.cards_one):
			end_game(game_id, user_id)
			page.redirect("/game/lose")
		else:
			end_game(game_id, user_id)
			this_user.cash += long(bet_amount)
			this_user.put()
			page.redirect("/game/win")