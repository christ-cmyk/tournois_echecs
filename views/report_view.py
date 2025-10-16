"""
Vue pour l'affichage des rapports (compactée < 100 lignes).
"""


class ReportView:
    def display_report_menu(self):
        print("\n📊 RAPPORTS")
        print("-" * 30)
        print("1. 📋 Tous les joueurs (ordre alphabétique)")
        print("2. 🏆 Tous les joueurs (par classement)")
        print("3. 🎯 Joueurs d'un tournoi (ordre alphabétique)")
        print("4. 🎯 Joueurs d'un tournoi (par classement)")
        print("5. 🏆 Liste de tous les tournois")
        print("6. 🔄 Rondes d'un tournoi")
        print("7. 🎮 Matchs d'un tournoi")
        print("0. ⬅️  Retour au menu principal")
        print("-" * 30)

    def display_report(self, report_content, title="RAPPORT"):
        print(f"\n📊 {title}")
        print("=" * 60)
        print(report_content)
        print("=" * 60)

    def display_tournament_selection_for_report(self, tournaments, report_type):
        if not tournaments:
            print("Aucun tournoi disponible pour ce rapport.")
            return None
        print(f"\n🎯 SÉLECTION DU TOURNOI POUR: {report_type}")
        print("-" * 50)
        for i, tournament in enumerate(tournaments, 1):
            status = "Terminé" if tournament.completed else "En cours"
            print(f"{i}. {tournament.name} - {tournament.location} ({status})")
        while True:
            try:
                choice = int(input("\nNuméro du tournoi (0 pour annuler): ").strip())
                if choice == 0:
                    return None
                if 1 <= choice <= len(tournaments):
                    return tournaments[choice - 1]
                print(f"❌ Veuillez entrer un nombre entre 0 et {len(tournaments)}")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")

    def display_no_tournaments_message(self):
        print("\n❌ Aucun tournoi enregistré.")
        print("Créez d'abord un tournoi pour générer ce rapport.")

    def display_no_players_message(self):
        print("\n❌ Aucun joueur enregistré.")
        print("Ajoutez d'abord des joueurs pour générer ce rapport.")

    def ask_save_report(self):
        return input(
            "\n💾 Voulez-vous sauvegarder ce rapport dans un fichier? (o/n): "
        ).strip().lower() in ['o', 'oui', 'y', 'yes']

    def get_report_filename(self, default_name="rapport.txt"):
        filename = input(f"\n📁 Nom du fichier (défaut: {default_name}): ").strip()
        return filename if filename else default_name

    def display_report_saved(self, filename):
        print(f"\n✅ Rapport sauvegardé dans: {filename}")

    def display_error_saving_report(self, filename):
        print(f"\n❌ Erreur lors de la sauvegarde du rapport: {filename}")
