"""
Defines and generates available web content.
"""
from flask import render_template, make_response
from rvr import APP
from rvr.infrastructure.ioc import FEATURES

@APP.route('/')
def start_page():
    """
    Generates the start page. AKA the main or home page.
    """
    matcher = FEATURES['GameFilter']
    matching_games = matcher.count_all()
    return render_template('start.html', title='Home',
        matching_games=matching_games)

@APP.route('/situation')
def situation_page():
    """
    Generates the situation selection page.
    """
    matcher = FEATURES['GameFilter']
    matching_games = matcher.count_all_situations()
    return render_template('situation.html',
        title='Select a Training Situation', matching_games=matching_games)

@APP.route('/texture')
def flop_texture_page():
    """
    Generates the flop texture selection page.
    """
    matcher = FEATURES['GameFilter']
    situation = None
    matching_games = matcher.count_situation(situation)
    return render_template('texture.html', title='Select a Flop Texture',
        matching_games=matching_games, situation="BB vs. a steal")

@APP.route('/preflop')
def preflop_page():
    """
    Generates the preflop situation selection page.
    """
    matcher = FEATURES['GameFilter']
    matching_games = matcher.count_all_preflop()
    return render_template('preflop.html', title='Select a Preflop Situation',
        matching_games=matching_games)

@APP.route('/open-games')
def open_games_page():
    """
    Generates a list of open games to choose from.
    """
    matcher = FEATURES['GameFilter']
    matching_games = matcher.all_games()
    return render_template('open_games.html', title='Select an Open Game',
        games=matching_games)

@APP.route('/confirmation')
def confirmation_page():
    """
    Generates a game start confirmation page. May be confirming new game, or
    join game.
    """
    return render_template('confirmation.html', title='Pre-Game Confirmation')

@APP.route('/game/not-started')
def game_not_started():
    """
    Generates the game page seen when game is not yet full.
    """
    return render_template('game_not_started.html', title='Game - Not Started')

@APP.route('/game/acting')
def game_acting():
    """
    Generates the game page seen when it's the current user's turn.
    """
    return render_template('game_acting.html', title='Game - Your Turn')

@APP.route('/game/waiting')
def game_waiting():
    """
    Generates the game page seen when it's the opponent's turn.
    """
    return render_template('game_waiting.html', title='Game - Waiting')

@APP.route('/robots.txt')
def robots_exclusion():
    """
    Provides robots.txt, to allow web crawlers to ignore some pages.
    """
    response = make_response(render_template('robots.txt'))
    response.headers['Content-Type'] = 'text/plain'
    return response