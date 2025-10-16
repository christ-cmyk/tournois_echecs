"""
Vue principale pour le menu de l'application
"""


class MainView:
    """Vue principale avec le menu de navigation"""
    
    def __init__(self):
        self.running = True
    
    def display_welcome(self):
        """Affiche le message de bienvenue"""
        print("=" * 60)
        print("🏆 GESTIONNAIRE DE TOURNOIS D'ÉCHECS 🏆")
        print("=" * 60)
        print("Application console autonome pour gérer les tournois")
        print("du Centre d'échecs")
        print("=" * 60)
    
    def display_main_menu(self):
        """Affiche le menu principal"""
        print("\n📋 MENU PRINCIPAL")
        print("-" * 30)
        print("1. 👥 Gestion des joueurs")
        print("2. 🏆 Gestion des tournois")
        print("3. 📊 Rapports")
        print("4. 💾 Sauvegarder")
        print("5. 📁 Charger")
        print("0. 🚪 Quitter")
        print("-" * 30)
    
    def get_user_choice(self, prompt="Votre choix: "):
        """
        Demande un choix à l'utilisateur
        
        Args:
            prompt (str): Message à afficher
        
        Returns:
            str: Choix de l'utilisateur
        """
        return input(prompt).strip()
    
    def display_error(self, message):
        """
        Affiche un message d'erreur
        
        Args:
            message (str): Message d'erreur
        """
        print(f"\n❌ ERREUR: {message}")
    
    def display_success(self, message):
        """
        Affiche un message de succès
        
        Args:
            message (str): Message de succès
        """
        print(f"\n✅ {message}")
    
    def display_info(self, message):
        """
        Affiche un message d'information
        
        Args:
            message (str): Message d'information
        """
        print(f"\nℹ️  {message}")
    
    def display_separator(self):
        """Affiche un séparateur"""
        print("-" * 50)
    
    def clear_screen(self):
        """Efface l'écran (fonctionne sur Windows, Mac et Linux)"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause(self):
        """Met en pause et attend une action de l'utilisateur"""
        input("\nAppuyez sur Entrée pour continuer...")
    
    def display_goodbye(self):
        """Affiche le message d'au revoir"""
        print("\n" + "=" * 60)
        print("👋 Merci d'avoir utilisé le Gestionnaire de Tournois d'Échecs!")
        print("À bientôt! 🏆")
        print("=" * 60)
    
    def confirm_action(self, message):
        """
        Demande confirmation pour une action
        
        Args:
            message (str): Message à confirmer
        
        Returns:
            bool: True si confirmé
        """
        response = input(f"{message} (o/n): ").strip().lower()
        return response in ['o', 'oui', 'y', 'yes']
