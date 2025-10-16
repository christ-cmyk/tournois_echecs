"""
Modèle Player pour représenter un joueur d'échecs
"""


class Player:
    """Classe représentant un joueur d'échecs"""
    
    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        """
        Initialise un joueur
        
        Args:
            last_name (str): Nom de famille
            first_name (str): Prénom
            birth_date (str): Date de naissance (format YYYY-MM-DD)
            gender (str): Sexe (M/F)
            ranking (int): Classement (nombre positif)
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.points = 0.0  # Points accumulés dans le tournoi actuel
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Classement: {self.ranking})"
    
    def __repr__(self):
        return f"Player('{self.last_name}', '{self.first_name}', '{self.birth_date}', '{self.gender}', {self.ranking})"
    
    def to_dict(self):
        """Convertit le joueur en dictionnaire pour la sérialisation"""
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'ranking': self.ranking,
            'points': self.points
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crée un joueur à partir d'un dictionnaire"""
        player = cls(
            data['last_name'],
            data['first_name'],
            data['birth_date'],
            data['gender'],
            data['ranking']
        )
        player.points = data.get('points', 0.0)
        return player
    
    def get_full_name(self):
        """Retourne le nom complet du joueur"""
        return f"{self.first_name} {self.last_name}"
    
    def update_ranking(self, new_ranking):
        """Met à jour le classement du joueur"""
        if new_ranking > 0:
            self.ranking = new_ranking
        else:
            raise ValueError("Le classement doit être un nombre positif")
    
    def add_points(self, points):
        """Ajoute des points au joueur"""
        self.points += points
    
    def reset_points(self):
        """Remet les points à zéro"""
        self.points = 0.0
