"""
Vue pour la gestion des tournois (composée de mixins).
"""

from views.mixins.tournament_view_menu import TournamentMenuMixin
from views.mixins.tournament_view_selection import TournamentSelectionMixin
from views.mixins.tournament_view_rounds import TournamentRoundsMixin


class TournamentView(TournamentMenuMixin, TournamentSelectionMixin, TournamentRoundsMixin):
    """Vue pour l'interface de gestion des tournois"""
    
    def get_tournament_data(self):
        """
        Demande les données d'un nouveau tournoi
        
        Returns:
            tuple: (nom, lieu, date_debut, date_fin, nb_tours, controle_temps, description)
        """
        print("\n➕ CRÉATION D'UN NOUVEAU TOURNOI")
        print("-" * 40)
        name = input("Nom du tournoi: ").strip()
        location = input("Lieu: ").strip()
        start_date = input("Date de début (YYYY-MM-DD): ").strip()
        end_date = input("Date de fin (YYYY-MM-DD, optionnel): ").strip()
        if not end_date:
            end_date = start_date
        while True:
            try:
                nb_rounds = int(input("Nombre de tours (défaut 4): ").strip() or "4")
                if nb_rounds <= 0:
                    raise ValueError("Le nombre de tours doit être positif")
                break
            except ValueError:
                print("❌ Veuillez entrer un nombre positif valide")
        print("Contrôle du temps (bullet/blitz/rapide): ", end="")
        time_control = input().strip().lower()
        if time_control not in ['bullet', 'blitz', 'rapide']:
            time_control = 'rapide'
        description = input("Description (optionnel): ").strip()
        return name, location, start_date, end_date, nb_rounds, time_control, description
