"""
Modèle Tournament pour représenter un tournoi d'échecs
"""

from models.round import Round


class Tournament:
    """Classe représentant un tournoi d'échecs"""
    
    def __init__(self, name, location, start_date, end_date=None, nb_rounds=4, 
                 time_control="rapide", description=""):
        """
        Initialise un tournoi
        
        Args:
            name (str): Nom du tournoi
            location (str): Lieu du tournoi
            start_date (str): Date de début (YYYY-MM-DD)
            end_date (str): Date de fin (YYYY-MM-DD) - optionnel
            nb_rounds (int): Nombre de tours (défaut: 4)
            time_control (str): Contrôle du temps (bullet/blitz/rapide)
            description (str): Description du tournoi
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date or start_date
        self.nb_rounds = nb_rounds
        self.time_control = time_control
        self.description = description
        self.players = []
        self.rounds = []
        self.completed = False
    
    def __str__(self):
        return f"{self.name} - {self.location} ({self.start_date})"
    
    def add_player(self, player):
        """
        Ajoute un joueur au tournoi
        
        Args:
            player (Player): Le joueur à ajouter
        """
        if len(self.players) >= 8:
            raise ValueError("Un tournoi ne peut pas avoir plus de 8 joueurs")
        
        if player not in self.players:
            self.players.append(player)
            player.reset_points()  # Remet les points à zéro pour le nouveau tournoi
    
    def remove_player(self, player):
        """
        Retire un joueur du tournoi
        
        Args:
            player (Player): Le joueur à retirer
        """
        if player in self.players:
            self.players.remove(player)
    
    def add_round(self, round_obj):
        """
        Ajoute une ronde au tournoi
        
        Args:
            round_obj (Round): La ronde à ajouter
        """
        self.rounds.append(round_obj)
    
    def get_current_round(self):
        """
        Retourne la ronde actuelle (la dernière créée non terminée)
        
        Returns:
            Round or None: La ronde actuelle ou None
        """
        for round_obj in reversed(self.rounds):
            if not round_obj.completed:
                return round_obj
        return None
    
    def get_players_by_ranking(self):
        """
        Retourne les joueurs triés par classement (décroissant)
        
        Returns:
            list: Liste des joueurs triés par classement
        """
        return sorted(self.players, key=lambda p: p.ranking, reverse=True)
    
    def get_players_by_points(self):
        """
        Retourne les joueurs triés par points (décroissant), puis par classement
        
        Returns:
            list: Liste des joueurs triés par points puis classement
        """
        return sorted(self.players, key=lambda p: (-p.points, -p.ranking))
    
    def is_full(self):
        """
        Vérifie si le tournoi a atteint le nombre maximum de joueurs
        
        Returns:
            bool: True si le tournoi est complet (8 joueurs)
        """
        return len(self.players) == 8
    
    def can_start(self):
        """
        Vérifie si le tournoi peut commencer (8 joueurs)
        
        Returns:
            bool: True si le tournoi peut commencer
        """
        return self.is_full()
    
    def complete_tournament(self):
        """Marque le tournoi comme terminé"""
        self.completed = True
    
    def to_dict(self):
        """Convertit le tournoi en dictionnaire pour la sérialisation"""
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'nb_rounds': self.nb_rounds,
            'time_control': self.time_control,
            'description': self.description,
            'players': [player.to_dict() for player in self.players],
            'rounds': [round_obj.to_dict() for round_obj in self.rounds],
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Crée un tournoi à partir d'un dictionnaire
        
        Args:
            data (dict): Données du tournoi
        """
        from models.player import Player
        
        tournament = cls(
            data['name'],
            data['location'],
            data['start_date'],
            data.get('end_date'),
            data.get('nb_rounds', 4),
            data.get('time_control', 'rapide'),
            data.get('description', '')
        )
        tournament.completed = data.get('completed', False)
        
        # Reconstruction des joueurs
        for player_data in data.get('players', []):
            player = Player.from_dict(player_data)
            tournament.players.append(player)
        
        # Reconstruction des rondes
        players_dict = {player.get_full_name(): player for player in tournament.players}
        for round_data in data.get('rounds', []):
            round_obj = Round.from_dict(round_data, players_dict)
            tournament.rounds.append(round_obj)
        
        return tournament
