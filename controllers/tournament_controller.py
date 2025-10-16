"""
Contrôleur Tournoi re-composé depuis des mixins pour rester < 100 lignes.
"""

from controllers.mixins.tournament_create import TournamentCreateMixin
from controllers.mixins.tournament_pairs import TournamentPairsMixin
from controllers.mixins.tournament_queries import TournamentQueriesMixin


class TournamentController(TournamentCreateMixin, TournamentPairsMixin, TournamentQueriesMixin):
    def __init__(self, player_controller):
        self.tournaments = []
        self.player_controller = player_controller
