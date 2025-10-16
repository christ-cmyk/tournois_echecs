"""
Mixins de vue Tournoi: sélections et ajouts de joueurs.
"""


class TournamentSelectionMixin:
    def get_tournament_selection(self, tournaments):
        """Sélectionne un tournoi dans une liste"""
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None
        print("\nSélectionnez un tournoi:")
        for i, tournament in enumerate(tournaments, 1):
            status = "Terminé" if tournament.completed else "En cours"
            print(f"{i}. {tournament.name} - {tournament.location} ({status})")
        while True:
            try:
                choice = int(input("\nNuméro du tournoi: ").strip())
                if 1 <= choice <= len(tournaments):
                    return tournaments[choice - 1]
                print(f"❌ Veuillez entrer un nombre entre 1 et {len(tournaments)}")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")

    def display_available_players(self, available_players, tournament_players):
        """Affiche les joueurs disponibles/présents"""
        print(f"\n👥 JOUEURS DANS LE TOURNOI ({len(tournament_players)}/8)")
        print("-" * 50)
        if tournament_players:
            for i, player in enumerate(tournament_players, 1):
                print(f"{i}. {player.get_full_name()} (Classement: {player.ranking})")
        else:
            print("Aucun joueur dans le tournoi.")
        print(f"\n👥 JOUEURS DISPONIBLES ({len(available_players)})")
        print("-" * 50)
        if available_players:
            for i, player in enumerate(available_players, 1):
                print(f"{i}. {player.get_full_name()} (Classement: {player.ranking})")
        else:
            print("Aucun joueur disponible.")

    def get_player_selection_for_tournament(self, available_players):
        """Choisit un joueur à ajouter au tournoi"""
        if not available_players:
            return None
        while True:
            try:
                choice = int(input("\nNuméro du joueur à ajouter (0 pour annuler): ").strip())
                if choice == 0:
                    return None
                if 1 <= choice <= len(available_players):
                    return available_players[choice - 1]
                print(f"❌ Veuillez entrer un nombre entre 0 et {len(available_players)}")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
