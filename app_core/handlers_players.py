"""
Handlers: actions liées aux joueurs (menus, ajouts, MAJ classement).
"""


class PlayersHandlers:
    def handle_player_management(self):
        while True:
            self.player_view.display_player_menu()
            choice = self.main_view.get_user_choice()
            if choice == "1":
                self.add_player()
            elif choice == "2":
                players = self.player_controller.get_all_players()
                self.player_view.display_players_list(players)
                self.main_view.pause()
            elif choice == "3":
                players = self.player_controller.get_players_by_ranking()
                self.player_view.display_players_ranking(players)
                self.main_view.pause()
            elif choice == "4":
                players = self.player_controller.get_players_alphabetically()
                self.player_view.display_players_alphabetical(players)
                self.main_view.pause()
            elif choice == "5":
                self.update_player_ranking()
            elif choice == "0":
                break
            else:
                self.main_view.display_error("Choix invalide.")

    def add_player(self):
        try:
            data = self.player_view.get_player_data()
            player = self.player_controller.add_player(*data)
            self.player_view.display_player_added(player)
            self.main_view.pause()
        except ValueError as e:
            self.main_view.display_error(str(e))
            self.main_view.pause()

    def update_player_ranking(self):
        players = self.player_controller.get_all_players()
        if not players:
            self.main_view.display_error("Aucun joueur enregistré.")
            self.main_view.pause()
            return
        player = self.player_view.get_player_selection(players)
        if player:
            try:
                new_ranking = self.player_view.get_new_ranking(player)
                self.player_controller.update_player_ranking(player, new_ranking)
                self.player_view.display_player_updated(player)
                self.main_view.pause()
            except ValueError as e:
                self.main_view.display_error(str(e))
                self.main_view.pause()
