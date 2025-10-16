"""
Mixins Tournoi: création et ajout de joueurs.
"""

from models.tournament import Tournament


class TournamentCreateMixin:
    def create_tournament(self, name, location, start_date, end_date=None,
                          nb_rounds=4, time_control="rapide", description=""):
        """
        Crée un nouveau tournoi
        """
        tournament = Tournament(
            name, location, start_date, end_date, nb_rounds, time_control, description
        )
        self.tournaments.append(tournament)
        return tournament

    def add_player_to_tournament(self, tournament, player):
        """Ajoute un joueur au tournoi"""
        tournament.add_player(player)
