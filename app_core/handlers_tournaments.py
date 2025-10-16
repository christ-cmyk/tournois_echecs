"""
Handlers: actions liées aux tournois (création, paires, résultats).
"""


class TournamentsHandlers:
    def handle_tournament_management(self):
        while True:
            self.tournament_view.display_tournament_menu()
            choice = self.main_view.get_user_choice()
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                tournaments = self.tournament_controller.get_all_tournaments()
                self.tournament_view.display_tournaments_list(tournaments)
                self.main_view.pause()
            elif choice == "3":
                self.play_tournament()
            elif choice == "4":
                self.add_players_to_tournament()
            elif choice == "5":
                self.generate_next_round()
            elif choice == "6":
                self.enter_round_results()
            elif choice == "7":
                self.complete_tournament()
            elif choice == "0":
                break
            else:
                self.main_view.display_error("Choix invalide.")

    def create_tournament(self):
        try:
            data = self.tournament_view.get_tournament_data()
            tournament = self.tournament_controller.create_tournament(*data)
            self.tournament_view.display_tournament_created(tournament)
            self.main_view.pause()
        except ValueError as e:
            self.main_view.display_error(str(e))
            self.main_view.pause()

    def play_tournament(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.tournament_view.get_tournament_selection(tournaments)
        if not tournament:
            return
        if not tournament.can_start():
            self.main_view.display_error("Le tournoi doit avoir 8 joueurs pour commencer.")
            self.main_view.pause()
            return
        if not tournament.rounds:
            try:
                self.tournament_controller.generate_first_round_pairs(tournament)
                self.main_view.display_success("Première ronde générée!")
            except ValueError as e:
                self.main_view.display_error(str(e))
                self.main_view.pause()
                return
        while len(tournament.rounds) < tournament.nb_rounds:
            current_round = tournament.get_current_round()
            if current_round and not current_round.completed:
                self.play_round(current_round)
            else:
                try:
                    self.tournament_controller.generate_next_round_pairs(tournament)
                    self.main_view.display_success(f"Ronde {len(tournament.rounds)} générée!")
                except ValueError as e:
                    self.main_view.display_error(str(e))
                    break
        self.main_view.display_success("Tournoi terminé!")
        self.tournament_controller.complete_tournament(tournament)
        self.tournament_view.display_tournament_completed(tournament)
        self.main_view.pause()

    def play_round(self, round_obj):
        self.tournament_view.display_round_matches(round_obj)
        for match in round_obj.matches:
            if not match.played:
                result = self.tournament_view.get_match_result(match)
                if result:
                    match.set_result(result[0], result[1])
                    self.main_view.display_success("Résultat enregistré!")
        if round_obj.is_all_matches_played():
            round_obj.end_round()
            self.main_view.display_success("Ronde terminée!")

    def add_players_to_tournament(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.tournament_view.get_tournament_selection(tournaments)
        if not tournament or tournament.is_full():
            if tournament and tournament.is_full():
                self.main_view.display_error("Le tournoi est complet (8 joueurs).")
            self.main_view.pause()
            return
        available = self.player_controller.get_available_players_for_tournament(
            tournament.players
        )
        while not tournament.is_full() and available:
            self.tournament_view.display_available_players(available, tournament.players)
            player = self.tournament_view.get_player_selection_for_tournament(available)
            if player:
                try:
                    self.tournament_controller.add_player_to_tournament(tournament, player)
                    self.main_view.display_success(f"{player.get_full_name()} ajouté au tournoi!")
                    available.remove(player)
                except ValueError as e:
                    self.main_view.display_error(str(e))
            else:
                break
            self.main_view.pause()

    def generate_next_round(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.tournament_view.get_tournament_selection(tournaments)
        if not tournament:
            return
        try:
            if not tournament.rounds:
                self.tournament_controller.generate_first_round_pairs(tournament)
                self.main_view.display_success("Première ronde générée!")
            else:
                self.tournament_controller.generate_next_round_pairs(tournament)
                self.main_view.display_success("Ronde suivante générée!")
            self.main_view.pause()
        except ValueError as e:
            self.main_view.display_error(str(e))
            self.main_view.pause()

    def enter_round_results(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.tournament_view.get_tournament_selection(tournaments)
        if not tournament or not tournament.rounds:
            if tournament and not tournament.rounds:
                self.main_view.display_error("Aucune ronde dans ce tournoi.")
            self.main_view.pause()
            return
        current_round = tournament.get_current_round()
        if not current_round:
            self.main_view.display_error("Toutes les rondes sont terminées.")
            self.main_view.pause()
            return
        self.play_round(current_round)
        self.main_view.pause()

    def complete_tournament(self):
        tournaments = self.tournament_controller.get_all_tournaments()
        tournament = self.tournament_view.get_tournament_selection(tournaments)
        if tournament and not tournament.completed:
            if self.main_view.confirm_action("Voulez-vous terminer ce tournoi?"):
                self.tournament_controller.complete_tournament(tournament)
                self.tournament_view.display_tournament_completed(tournament)
                self.main_view.pause()
