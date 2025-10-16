"""
Modèle Match pour représenter un match d'échecs
"""


class Match:
    """Classe représentant un match entre deux joueurs"""
    
    def __init__(self, player1, player2):
        """
        Initialise un match
        
        Args:
            player1 (Player): Premier joueur
            player2 (Player): Deuxième joueur
        """
        self.player1 = player1
        self.player2 = player2
        self.score1 = None  # Score du joueur 1 (0, 0.5, ou 1)
        self.score2 = None  # Score du joueur 2 (0, 0.5, ou 1)
        self.played = False
    
    def __str__(self):
        if self.played:
            return f"{self.player1.get_full_name()} ({self.score1}) - {self.player2.get_full_name()} ({self.score2})"
        else:
            return f"{self.player1.get_full_name()} - {self.player2.get_full_name()}"
    
    def set_result(self, score1, score2):
        """
        Définit le résultat du match
        
        Args:
            score1 (float): Score du joueur 1 (0, 0.5, ou 1)
            score2 (float): Score du joueur 2 (0, 0.5, ou 1)
        """
        if score1 not in [0, 0.5, 1] or score2 not in [0, 0.5, 1]:
            raise ValueError("Les scores doivent être 0, 0.5 ou 1")
        
        if abs(score1 + score2 - 1.0) > 0.01:  # Tolérance pour les erreurs de float
            raise ValueError("La somme des scores doit être égale à 1")
        
        self.score1 = score1
        self.score2 = score2
        self.played = True
        
        # Mise à jour des points des joueurs
        self.player1.add_points(score1)
        self.player2.add_points(score2)
    
    def to_tuple(self):
        """
        Retourne le match sous forme de tuple comme demandé dans les spécifications
        
        Returns:
            tuple: ([player1, score1], [player2, score2])
        """
        return ([self.player1, self.score1], [self.player2, self.score2])
    
    def to_dict(self):
        """Convertit le match en dictionnaire pour la sérialisation"""
        return {
            'player1': self.player1.to_dict() if self.player1 else None,
            'player2': self.player2.to_dict() if self.player2 else None,
            'score1': self.score1,
            'score2': self.score2,
            'played': self.played
        }
    
    @classmethod
    def from_dict(cls, data, players_dict):
        """
        Crée un match à partir d'un dictionnaire
        
        Args:
            data (dict): Données du match
            players_dict (dict): Dictionnaire des joueurs indexés par leur nom complet
        """
        match = cls(None, None)
        match.score1 = data.get('score1')
        match.score2 = data.get('score2')
        match.played = data.get('played', False)
        
        if data.get('player1'):
            player1_key = f"{data['player1']['first_name']} {data['player1']['last_name']}"
            match.player1 = players_dict.get(player1_key)
        
        if data.get('player2'):
            player2_key = f"{data['player2']['first_name']} {data['player2']['last_name']}"
            match.player2 = players_dict.get(player2_key)
        
        return match
