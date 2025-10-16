"""
Handlers: affichage et génération des rapports.
"""


class ReportsHandlers:
    def handle_reports(self):
        while True:
            self.report_view.display_report_menu()
            choice = self.main_view.get_user_choice()
            if choice == "1":
                report = self.report_controller.generate_all_players_report_alphabetical()
                self.report_view.display_report(report, "JOUEURS PAR ORDRE ALPHABÉTIQUE")
                self.main_view.pause()
            elif choice == "2":
                report = self.report_controller.generate_all_players_report_by_ranking()
                self.report_view.display_report(report, "JOUEURS PAR CLASSEMENT")
                self.main_view.pause()
            elif choice == "3":
                self.show_tournament_players_report_alphabetical()
            elif choice == "4":
                self.show_tournament_players_report_by_ranking()
            elif choice == "5":
                report = self.report_controller.generate_all_tournaments_report()
                self.report_view.display_report(report, "TOUS LES TOURNOIS")
                self.main_view.pause()
            elif choice == "6":
                self.show_tournament_rounds_report()
            elif choice == "7":
                self.show_tournament_matches_report()
            elif choice == "0":
                break
            else:
                self.main_view.display_error("Choix invalide.")

    def show_tournament_players_report_alphabetical(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.report_view.display_tournament_selection_for_report(
            tournaments, "JOUEURS PAR ORDRE ALPHABÉTIQUE"
        )
        if tournament:
            report = self.report_controller.generate_tournament_players_report_alphabetical(tournament)
            self.report_view.display_report(report, f"JOUEURS DE '{tournament.name}' (ALPHABÉTIQUE)")
            self.main_view.pause()

    def show_tournament_players_report_by_ranking(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.report_view.display_tournament_selection_for_report(
            tournaments, "JOUEURS PAR CLASSEMENT"
        )
        if tournament:
            report = self.report_controller.generate_tournament_players_report_by_ranking(tournament)
            self.report_view.display_report(report, f"JOUEURS DE '{tournament.name}' (CLASSEMENT)")
            self.main_view.pause()

    def show_tournament_rounds_report(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.report_view.display_tournament_selection_for_report(
            tournaments, "RONDES DU TOURNOI"
        )
        if tournament:
            report = self.report_controller.generate_tournament_rounds_report(tournament)
            self.report_view.display_report(report, f"RONDES DE '{tournament.name}'")
            self.main_view.pause()

    def show_tournament_matches_report(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.report_view.display_tournament_selection_for_report(
            tournaments, "MATCHS DU TOURNOI"
        )
        if tournament:
            report = self.report_controller.generate_tournament_matches_report(tournament)
            self.report_view.display_report(report, f"MATCHS DE '{tournament.name}'")
            self.main_view.pause()
