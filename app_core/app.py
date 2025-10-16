"""
Application: composition et boucle principale (menu).
Découpage pour maintenir chaque fichier < 100 lignes.
"""

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from views.main_view import MainView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.report_view import ReportView
from app_core.handlers_players import PlayersHandlers
from app_core.handlers_tournaments import TournamentsHandlers
from app_core.handlers_reports import ReportsHandlers


class ChessTournamentApp(PlayersHandlers, TournamentsHandlers, ReportsHandlers):
    def __init__(self):
        # Contrôleurs
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller)
        self.report_controller = ReportController(
            self.player_controller, self.tournament_controller
        )

        # Vues
        self.main_view = MainView()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.report_view = ReportView()

        self.running = True

    def run(self):
        self.main_view.display_welcome()
        while self.running:
            self.main_view.display_main_menu()
            choice = self.main_view.get_user_choice()
            if choice == "1":
                self.handle_player_management()
            elif choice == "2":
                self.handle_tournament_management()
            elif choice == "3":
                self.handle_reports()
            elif choice == "4":
                self.save_data()
            elif choice == "5":
                self.load_data()
            elif choice == "0":
                self.main_view.display_goodbye()
                self.running = False
            else:
                self.main_view.display_error("Choix invalide. Veuillez réessayer.")

    def save_data(self):
        self.main_view.display_info("Sauvegarde TinyDB à implémenter")
        self.main_view.pause()

    def load_data(self):
        self.main_view.display_info("Chargement TinyDB à implémenter")
        self.main_view.pause()


def main():
    app = ChessTournamentApp()
    app.run()
