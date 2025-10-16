"""
Vue pour la gestion des joueurs (découpée en mixins locales).
"""


class PlayerMenuMixin:
    def display_player_menu(self):
        print("\n👥 GESTION DES JOUEURS")
        print("-" * 30)
        print("1. ➕ Ajouter un joueur")
        print("2. 📋 Lister tous les joueurs")
        print("3. 📊 Lister par classement")
        print("4. 🔤 Lister par ordre alphabétique")
        print("5. ✏️  Modifier un classement")
        print("0. ⬅️  Retour au menu principal")
        print("-" * 30)


class PlayerFormMixin:
    def get_player_data(self):
        """
        Demande les données d'un nouveau joueur
        
        Returns:
            tuple: (nom, prénom, date_naissance, sexe, classement)
        """
        print("\n➕ AJOUT D'UN NOUVEAU JOUEUR")
        print("-" * 30)
        
        last_name = input("Nom de famille: ").strip()
        first_name = input("Prénom: ").strip()
        birth_date = input("Date de naissance (YYYY-MM-DD): ").strip()
        
        print("Sexe (M/F): ", end="")
        gender = input().strip().upper()
        
        while True:
            try:
                ranking = int(input("Classement (nombre positif): ").strip())
                if ranking <= 0:
                    raise ValueError("Le classement doit être positif")
                break
            except ValueError:
                print("❌ Veuillez entrer un nombre positif valide")
        
        return last_name, first_name, birth_date, gender, ranking


class PlayerListMixin:
    def display_players_list(self, players, title="LISTE DES JOUEURS"):
        """
        Affiche la liste des joueurs
        
        Args:
            players (list): Liste des joueurs
            title (str): Titre à afficher
        """
        print(f"\n📋 {title}")
        print("=" * 60)
        
        if not players:
            print("Aucun joueur enregistré.")
        else:
            for i, player in enumerate(players, 1):
                print(f"{i:2d}. {player.get_full_name():<30} "
                      f"Classement: {player.ranking:4d} "
                      f"Sexe: {player.gender} "
                      f"Né(e) le: {player.birth_date}")

    def display_players_ranking(self, players):
        """Affiche la liste des joueurs par classement"""
        self.display_players_list(players, "JOUEURS PAR CLASSEMENT")

    def display_players_alphabetical(self, players):
        """Affiche la liste des joueurs par ordre alphabétique"""
        self.display_players_list(players, "JOUEURS PAR ORDRE ALPHABÉTIQUE")


class PlayerSelectionMixin:
    def get_player_selection(self, players):
        """
        Permet à l'utilisateur de sélectionner un joueur
        
        Args:
            players (list): Liste des joueurs
        
        Returns:
            Player or None: Joueur sélectionné ou None
        """
        if not players:
            print("Aucun joueur disponible.")
            return None
        
        print("\nSélectionnez un joueur:")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player.get_full_name()} (Classement: {player.ranking})")
        
        while True:
            try:
                choice = int(input("\nNuméro du joueur: ").strip())
                if 1 <= choice <= len(players):
                    return players[choice - 1]
                else:
                    print(f"❌ Veuillez entrer un nombre entre 1 et {len(players)}")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")

    def get_new_ranking(self, player):
        """
        Demande le nouveau classement pour un joueur
        
        Args:
            player (Player): Le joueur à modifier
        
        Returns:
            int: Nouveau classement
        """
        print("\n✏️  MODIFICATION DU CLASSEMENT")
        print(f"Joueur: {player.get_full_name()}")
        print(f"Classement actuel: {player.ranking}")
        
        while True:
            try:
                new_ranking = int(input("Nouveau classement: ").strip())
                if new_ranking <= 0:
                    raise ValueError("Le classement doit être positif")
                return new_ranking
            except ValueError:
                print("❌ Veuillez entrer un nombre positif valide")


class PlayerFeedbackMixin:
    def display_player_updated(self, player):
        """
        Confirme la mise à jour d'un joueur
        
        Args:
            player (Player): Le joueur mis à jour
        """
        print(f"\n✅ Classement de {player.get_full_name()} mis à jour: {player.ranking}")

    def display_player_added(self, player):
        """
        Confirme l'ajout d'un joueur
        
        Args:
            player (Player): Le joueur ajouté
        """
        print(f"\n✅ Joueur ajouté: {player.get_full_name()} (Classement: {player.ranking})")


class PlayerView(
    PlayerMenuMixin,
    PlayerFormMixin,
    PlayerListMixin,
    PlayerSelectionMixin,
    PlayerFeedbackMixin,
):
    """Vue principale Joueur composée de mixins"""
    pass
