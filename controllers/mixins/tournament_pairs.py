"""
Mixins Tournoi: génération des paires (système suisse).
"""

from models.round import Round
from models.match import Match


class TournamentPairsMixin:
    def generate_first_round_pairs(self, tournament):
        if len(tournament.players) != 8:
            raise ValueError("Un tournoi doit avoir exactement 8 joueurs")
        players_sorted = tournament.get_players_by_ranking()
        top_half = players_sorted[:4]
        bottom_half = players_sorted[4:]
        round_name = f"Round {len(tournament.rounds) + 1}"
        new_round = Round(round_name)
        new_round.start_round()
        for i in range(4):
            match = Match(top_half[i], bottom_half[i])
            new_round.add_match(match)
        tournament.add_round(new_round)
        return new_round

    def generate_next_round_pairs(self, tournament):
        if len(tournament.players) != 8:
            raise ValueError("Un tournoi doit avoir exactement 8 joueurs")
        players_sorted = tournament.get_players_by_points()
        round_name = f"Round {len(tournament.rounds) + 1}"
        new_round = Round(round_name)
        new_round.start_round()
        used_players = set()
        for i in range(0, 8, 2):
            player1 = players_sorted[i]
            player2 = players_sorted[i + 1]
            if self._have_played_before(tournament, player1, player2):
                player2 = self._find_next_available_opponent(
                    tournament, player1, used_players, players_sorted
                )
            match = Match(player1, player2)
            new_round.add_match(match)
            used_players.add(player1)
            used_players.add(player2)
        tournament.add_round(new_round)
        return new_round

    def _have_played_before(self, tournament, player1, player2):
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                if (
                    (match.player1 == player1 and match.player2 == player2)
                    or (match.player1 == player2 and match.player2 == player1)
                ):
                    return True
        return False

    def _find_next_available_opponent(self, tournament, player, used_players, players_sorted):
        for potential_opponent in players_sorted:
            cond_not_same = potential_opponent != player
            cond_not_used = potential_opponent not in used_players
            cond_not_played = not self._have_played_before(
                tournament, player, potential_opponent
            )
            if cond_not_same and cond_not_used and cond_not_played:
                return potential_opponent
        for potential_opponent in players_sorted:
            if potential_opponent != player and potential_opponent not in used_players:
                return potential_opponent
        return players_sorted[1]
