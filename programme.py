"""
Point d'entrée minimal de l'application console.
La logique de l'application est déplacée dans app_core/ pour respecter < 100 lignes/fichier.
"""

from app_core.app import main


if __name__ == "__main__":
    main()
