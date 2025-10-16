"""
Modèle Round pour représenter une ronde d'un tournoi
"""

from datetime import datetime
from models.match import Match


class Round:
    """Classe représentant une ronde d'un tournoi"""
    
    def __init__(self, name):
        """
        Initialise une ronde
        
        Args:
            name (str): Nom de la ronde (ex: "Round 1")
        """
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []
        self.completed = False
    
    def __str__(self):
        return f"{self.name} - {'Terminé' if self.completed else 'En cours'}"
    
    def start_round(self):
        """Démarre la ronde (enregistre l'heure de début)"""
        self.start_time = datetime.now()
        self.completed = False
    
    def end_round(self):
        """Termine la ronde (enregistre l'heure de fin)"""
        self.end_time = datetime.now()
        self.completed = True
    
    def add_match(self, match):
        """
        Ajoute un match à la ronde
        
        Args:
            match (Match): Le match à ajouter
        """
        self.matches.append(match)
    
    def is_all_matches_played(self):
        """
        Vérifie si tous les matchs de la ronde ont été joués
        
        Returns:
            bool: True si tous les matchs sont terminés
        """
        return all(match.played for match in self.matches)
    
    def get_matches_as_tuples(self):
        """
        Retourne tous les matchs sous forme de tuples
        
        Returns:
            list: Liste de tuples ([player1, score1], [player2, score2])
        """
        return [match.to_tuple() for match in self.matches if match.played]
    
    def to_dict(self):
        """Convertit la ronde en dictionnaire pour la sérialisation"""
        return {
            'name': self.name,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'matches': [match.to_dict() for match in self.matches],
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data, players_dict):
        """
        Crée une ronde à partir d'un dictionnaire
        
        Args:
            data (dict): Données de la ronde
            players_dict (dict): Dictionnaire des joueurs indexés par leur nom complet
        """
        round_obj = cls(data['name'])
        round_obj.completed = data.get('completed', False)
        
        if data.get('start_time'):
            round_obj.start_time = datetime.fromisoformat(data['start_time'])
        
        if data.get('end_time'):
            round_obj.end_time = datetime.fromisoformat(data['end_time'])
        
        # Reconstruction des matchs
        for match_data in data.get('matches', []):
            match = Match.from_dict(match_data, players_dict)
            round_obj.add_match(match)
        
        return round_obj
