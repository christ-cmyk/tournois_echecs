"""
Mixins de vue Tournoi: menu et affichage liste/états.
"""


class TournamentMenuMixin:
    def display_tournament_menu(self):
        """Affiche le menu de gestion des tournois"""
        print("\n🏆 GESTION DES TOURNOIS")
        print("-" * 30)
        print("1. ➕ Créer un tournoi")
        print("2. 📋 Lister tous les tournois")
        print("3. 🎮 Jouer un tournoi")
        print("4. 👥 Ajouter des joueurs à un tournoi")
        print("5. 🔄 Générer les paires du tour suivant")
        print("6. 📝 Saisir les résultats d'un tour")
        print("7. ✅ Terminer un tournoi")
        print("0. ⬅️  Retour au menu principal")
        print("-" * 30)

    def display_tournaments_list(self, tournaments):
        """Affiche la liste des tournois"""
        print("\n🏆 LISTE DES TOURNOIS")
        print("=" * 60)
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        for i, tournament in enumerate(tournaments, 1):
            status = "✅ Terminé" if tournament.completed else "🔄 En cours"
            print(f"{i:2d}. {tournament.name}")
            print(f"     Lieu: {tournament.location}")
            print(f"     Date: {tournament.start_date}")
            if tournament.end_date != tournament.start_date:
                print(f"           au {tournament.end_date}")
            print(f"     Contrôle: {tournament.time_control}")
            print(f"     Statut: {status}")
            print(f"     Joueurs: {len(tournament.players)}/8")
            print()

    def display_tournament_created(self, tournament):
        """Confirme la création d'un tournoi"""
        print(f"\n✅ Tournoi créé: {tournament.name}")
        print(f"   Lieu: {tournament.location}")
        print(f"   Date: {tournament.start_date}")
        print(f"   Tours: {tournament.nb_rounds}")

    def display_tournament_status(self, tournament):
        """Affiche le statut d'un tournoi"""
        print(f"\n📊 STATUT DU TOURNOI: {tournament.name}")
        print("-" * 50)
        print(f"Joueurs: {len(tournament.players)}/8")
        print(f"Rondes: {len(tournament.rounds)}/{tournament.nb_rounds}")
        if tournament.rounds:
            current_round = tournament.get_current_round()
            if current_round:
                print(f"Ronde actuelle: {current_round.name}")
            else:
                print("Toutes les rondes sont terminées.")
