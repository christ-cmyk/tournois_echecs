"""
Contrôleur pour la génération des rapports
"""


class ReportController:
    """Contrôleur pour générer les rapports"""
    
    def __init__(self, player_controller, tournament_controller):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller
    
    def generate_all_players_report_alphabetical(self):
        """
        Génère le rapport de tous les joueurs par ordre alphabétique
        
        Returns:
            str: Rapport formaté
        """
        players = self.player_controller.get_players_alphabetically()
        
        report = ("=== RAPPORT DE TOUS LES JOUEURS "
                  "(ORDRE ALPHABÉTIQUE) ===\n\n")
        
        if not players:
            report += "Aucun joueur enregistré.\n"
        else:
            for i, player in enumerate(players, 1):
                try:
                    full_name = f"{player.first_name} {player.last_name}"
                    report += (f"{i:2d}. {full_name:<30} "
                               f"Classement: {player.ranking:4d} "
                               f"Sexe: {player.gender} "
                               f"Né(e) le: {player.birth_date}\n")
                except AttributeError as e:
                    error_msg = f"Erreur lors de l'affichage du joueur {i}: {e}"
                    report += f"{error_msg}\n"
        
        return report
    
    def generate_all_players_report_by_ranking(self):
        """
        Génère le rapport de tous les joueurs par classement
        
        Returns:
            str: Rapport formaté
        """
        players = self.player_controller.get_players_by_ranking()
        
        report = ("=== RAPPORT DE TOUS LES JOUEURS "
                  "(PAR CLASSEMENT) ===\n\n")
        
        if not players:
            report += "Aucun joueur enregistré.\n"
        else:
            for i, player in enumerate(players, 1):
                try:
                    full_name = f"{player.first_name} {player.last_name}"
                    report += (f"{i:2d}. {full_name:<30} "
                               f"Classement: {player.ranking:4d} "
                               f"Points: {player.points:.1f} "
                               f"Sexe: {player.gender} "
                               f"Né(e) le: {player.birth_date}\n")
                except AttributeError as e:
                    error_msg = f"Erreur lors de l'affichage du joueur {i}: {e}"
                    report += f"{error_msg}\n"
        
        return report
    
    def generate_tournament_players_report_alphabetical(self, tournament):
        """
        Génère le rapport des joueurs d'un tournoi par ordre alphabétique
        
        Args:
            tournament (Tournament): Le tournoi
        
        Returns:
            str: Rapport formaté
        """
        players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
        
        report = f"=== JOUEURS DU TOURNOI '{tournament.name}' (ORDRE ALPHABÉTIQUE) ===\n\n"
        
        if not players:
            report += "Aucun joueur dans ce tournoi.\n"
        else:
            for i, player in enumerate(players, 1):
                report += f"{i:2d}. {player.get_full_name():<30} "
                report += f"Classement: {player.ranking:4d}\n"
        
        return report
    
    def generate_tournament_players_report_by_ranking(self, tournament):
        """
        Génère le rapport des joueurs d'un tournoi par classement
        
        Args:
            tournament (Tournament): Le tournoi
        
        Returns:
            str: Rapport formaté
        """
        players = tournament.get_players_by_ranking()
        
        report = f"=== JOUEURS DU TOURNOI '{tournament.name}' (PAR CLASSEMENT) ===\n\n"
        
        if not players:
            report += "Aucun joueur dans ce tournoi.\n"
        else:
            for i, player in enumerate(players, 1):
                report += f"{i:2d}. {player.get_full_name():<30} "
                report += f"Classement: {player.ranking:4d}\n"
        
        return report
    
    def generate_all_tournaments_report(self):
        """
        Génère le rapport de tous les tournois
        
        Returns:
            str: Rapport formaté
        """
        tournaments = self.tournament_controller.get_all_tournaments()
        
        report = "=== RAPPORT DE TOUS LES TOURNOIS ===\n\n"
        
        if not tournaments:
            report += "Aucun tournoi enregistré.\n"
        else:
            for i, tournament in enumerate(tournaments, 1):
                status = "Terminé" if tournament.completed else "En cours"
                report += f"{i:2d}. {tournament.name}\n"
                report += f"     Lieu: {tournament.location}\n"
                report += f"     Date: {tournament.start_date}"
                if tournament.end_date != tournament.start_date:
                    report += f" au {tournament.end_date}"
                report += f"\n     Contrôle: {tournament.time_control}\n"
                report += f"     Statut: {status}\n"
                report += f"     Joueurs: {len(tournament.players)}/8\n\n"
        
        return report
    
    def generate_tournament_rounds_report(self, tournament):
        """
        Génère le rapport des rondes d'un tournoi
        
        Args:
            tournament (Tournament): Le tournoi
        
        Returns:
            str: Rapport formaté
        """
        report = f"=== RONDES DU TOURNOI '{tournament.name}' ===\n\n"
        
        if not tournament.rounds:
            report += "Aucune ronde dans ce tournoi.\n"
        else:
            for round_obj in tournament.rounds:
                report += f"{round_obj.name}:\n"
                start_txt = (
                    round_obj.start_time.strftime('%d/%m/%Y %H:%M')
                    if round_obj.start_time else 'Non démarré'
                )
                end_txt = (
                    round_obj.end_time.strftime('%d/%m/%Y %H:%M')
                    if round_obj.end_time else 'En cours'
                )
                report += f"  Début: {start_txt}\n"
                report += f"  Fin: {end_txt}\n"
                report += f"  Statut: {'Terminé' if round_obj.completed else 'En cours'}\n\n"
        
        return report
    
    def generate_tournament_matches_report(self, tournament):
        """
        Génère le rapport des matchs d'un tournoi
        
        Args:
            tournament (Tournament): Le tournoi
        
        Returns:
            str: Rapport formaté
        """
        report = f"=== MATCHS DU TOURNOI '{tournament.name}' ===\n\n"
        
        if not tournament.rounds:
            report += "Aucun match dans ce tournoi.\n"
        else:
            for round_obj in tournament.rounds:
                report += f"{round_obj.name}:\n"
                if not round_obj.matches:
                    report += "  Aucun match.\n\n"
                else:
                    for match in round_obj.matches:
                        if match.played:
                            report += f"  {match.player1.get_full_name()} ({match.score1}) - "
                            report += f"{match.player2.get_full_name()} ({match.score2})\n"
                        else:
                            left_name = match.player1.get_full_name()
                            right_name = match.player2.get_full_name()
                            report += f"  {left_name} - {right_name} (Non joué)\n"
                    report += "\n"
        
        return report
