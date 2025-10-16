"""
Contrôleur pour la gestion des joueurs
"""

from models.player import Player


class PlayerController:
    """Contrôleur pour gérer les opérations sur les joueurs"""
    
    def __init__(self):
        self.players = []
    
    def add_player(self, last_name, first_name, birth_date, gender, ranking):
        """
        Ajoute un nouveau joueur
        
        Args:
            last_name (str): Nom de famille
            first_name (str): Prénom
            birth_date (str): Date de naissance
            gender (str): Sexe (M/F)
            ranking (int): Classement
        
        Returns:
            Player: Le joueur créé
        """
        # Validation des données
        if not last_name or not first_name:
            raise ValueError("Le nom et prénom sont obligatoires")
        
        if gender.upper() not in ['M', 'F']:
            raise ValueError("Le sexe doit être M ou F")
        
        if not isinstance(ranking, int) or ranking <= 0:
            raise ValueError("Le classement doit être un nombre positif")
        
        # Vérification que le joueur n'existe pas déjà
        for player in self.players:
            if (
                player.last_name.lower() == last_name.lower()
                and player.first_name.lower() == first_name.lower()
            ):
                raise ValueError("Ce joueur existe déjà")
        
        player = Player(last_name, first_name, birth_date, gender.upper(), ranking)
        self.players.append(player)
        return player
    
    def get_all_players(self):
        """
        Retourne tous les joueurs
        
        Returns:
            list: Liste de tous les joueurs
        """
        return self.players.copy()
    
    def get_players_by_ranking(self):
        """
        Retourne les joueurs triés par classement (décroissant)
        
        Returns:
            list: Liste des joueurs triés par classement
        """
        return sorted(self.players, key=lambda p: p.ranking, reverse=True)
    
    def get_players_alphabetically(self):
        """
        Retourne les joueurs triés par ordre alphabétique
        
        Returns:
            list: Liste des joueurs triés par ordre alphabétique
        """
        return sorted(self.players, key=lambda p: (p.last_name, p.first_name))
    
    def find_player_by_name(self, last_name, first_name):
        """
        Trouve un joueur par son nom
        
        Args:
            last_name (str): Nom de famille
            first_name (str): Prénom
        
        Returns:
            Player or None: Le joueur trouvé ou None
        """
        for player in self.players:
            if (
                player.last_name.lower() == last_name.lower()
                and player.first_name.lower() == first_name.lower()
            ):
                return player
        return None
    
    def update_player_ranking(self, player, new_ranking):
        """
        Met à jour le classement d'un joueur
        
        Args:
            player (Player): Le joueur à modifier
            new_ranking (int): Nouveau classement
        """
        if not isinstance(new_ranking, int) or new_ranking <= 0:
            raise ValueError("Le classement doit être un nombre positif")
        
        player.update_ranking(new_ranking)
    
    def get_player_count(self):
        """
        Retourne le nombre de joueurs
        
        Returns:
            int: Nombre de joueurs
        """
        return len(self.players)
    
    def get_available_players_for_tournament(self, tournament_players):
        """
        Retourne les joueurs disponibles pour un tournoi
        
        Args:
            tournament_players (list): Liste des joueurs déjà dans le tournoi
        
        Returns:
            list: Liste des joueurs disponibles
        """
        return [player for player in self.players if player not in tournament_players]
