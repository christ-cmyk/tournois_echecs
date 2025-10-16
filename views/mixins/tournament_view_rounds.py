"""
Mixins de vue Tournoi: rondes, matchs et résultats.
"""


class TournamentRoundsMixin:
    def display_round_matches(self, round_obj):
        """Affiche les matchs d'une ronde"""
        print(f"\n🎮 {round_obj.name}")
        print("-" * 50)
        if not round_obj.matches:
            print("Aucun match dans cette ronde.")
            return
        for i, match in enumerate(round_obj.matches, 1):
            if match.played:
                print(
                    f"{i}. {match.player1.get_full_name()} ({match.score1}) - "
                    f"{match.player2.get_full_name()} ({match.score2})"
                )
            else:
                print(
                    f"{i}. {match.player1.get_full_name()} - {match.player2.get_full_name()}"
                )

    def get_match_result(self, match):
        """Demande le résultat d'un match"""
        print("\n📝 Résultat du match:")
        print(f"{match.player1.get_full_name()} vs {match.player2.get_full_name()}")
        print("\nOptions:")
        print("1. Victoire de " + match.player1.get_full_name())
        print("2. Victoire de " + match.player2.get_full_name())
        print("3. Match nul")
        print("0. Annuler")
        while True:
            try:
                choice = int(input("\nVotre choix: ").strip())
                if choice == 0:
                    return None
                if choice == 1:
                    return 1.0, 0.0
                if choice == 2:
                    return 0.0, 1.0
                if choice == 3:
                    return 0.5, 0.5
                print("❌ Veuillez entrer un choix entre 0 et 3")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")

    def display_tournament_completed(self, tournament):
        """Affiche le classement final"""
        print(f"\n🏆 TOURNOI TERMINÉ: {tournament.name}")
        print("=" * 50)
        players_sorted = tournament.get_players_by_points()
        print("🏅 CLASSEMENT FINAL:")
        for i, player in enumerate(players_sorted, 1):
            print(f"{i}. {player.get_full_name()} - {player.points} point(s)")
