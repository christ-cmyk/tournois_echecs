"""
Mixins Tournoi: requêtes et complétion.
"""


class TournamentQueriesMixin:
    def complete_tournament(self, tournament):
        tournament.complete_tournament()
        current_round = tournament.get_current_round()
        if current_round and not current_round.completed:
            current_round.end_round()

    def get_all_tournaments(self):
        return self.tournaments.copy()

    def get_tournament_by_name(self, name):
        for tournament in self.tournaments:
            if tournament.name.lower() == name.lower():
                return tournament
        return None
