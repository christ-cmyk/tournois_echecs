# 🏆 Gestionnaire de Tournois d'Échecs

Application console autonome en Python pour gérer les tournois d'échecs du Centre, compatible Windows, Mac et Linux.

## 📋 Fonctionnalités

- ✅ **Gestion des joueurs** : Ajout, modification des classements, listes triées
- ✅ **Gestion des tournois** : Création, ajout de joueurs, génération des paires
- ✅ **Système suisse** : Génération automatique des paires selon les règles
- ✅ **Gestion des matchs** : Saisie des résultats, attribution des points
- ✅ **Rapports complets** : Listes des joueurs, tournois, rondes et matchs
- ✅ **Interface intuitive** : Menus console clairs et faciles à utiliser

## 🛠️ Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   # Si vous avez git
   git clone <url-du-repo>
   cd tournois_echecs
   
   # Ou décompresser l'archive dans un dossier
   ```

2. **Créer et activer l'environnement virtuel**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Exécution

Une fois l'environnement virtuel activé :

```bash
python programme.py
```

L'application se lance avec un menu principal vous permettant d'accéder à toutes les fonctionnalités.

## 📁 Structure du projet

```
tournois_echecs/
├── programme.py              # Point d'entrée principal
├── requirements.txt          # Dépendances Python
├── README.md                # Ce fichier
├── models/                  # Modèles de données
│   ├── __init__.py
│   ├── player.py           # Modèle Joueur
│   ├── tournament.py       # Modèle Tournoi
│   ├── round.py           # Modèle Ronde
│   └── match.py           # Modèle Match
├── controllers/            # Logique métier
│   ├── __init__.py
│   ├── player_controller.py    # Contrôleur Joueurs
│   ├── tournament_controller.py # Contrôleur Tournois
│   └── report_controller.py    # Contrôleur Rapports
└── views/                  # Interface utilisateur
    ├── __init__.py
    ├── main_view.py        # Vue principale
    ├── player_view.py      # Vue Joueurs
    ├── tournament_view.py  # Vue Tournois
    └── report_view.py      # Vue Rapports
```

## 🎮 Guide d'utilisation

### 1. Gestion des joueurs
- **Ajouter un joueur** : Nom, prénom, date de naissance, sexe, classement
- **Lister les joueurs** : Par ordre alphabétique ou par classement
- **Modifier un classement** : Mise à jour des classements à tout moment

### 2. Gestion des tournois
- **Créer un tournoi** : Nom, lieu, dates, nombre de tours, contrôle du temps
- **Ajouter des joueurs** : Sélection parmi les joueurs disponibles (max 8)
- **Jouer un tournoi** : Génération automatique des paires et saisie des résultats
- **Générer les paires** : Système suisse pour les tours suivants

### 3. Système de points
- **Victoire** : 1 point
- **Défaite** : 0 point
- **Match nul** : 0,5 point chacun

### 4. Rapports disponibles
- Liste de tous les joueurs (alphabétique/classement)
- Liste des joueurs d'un tournoi
- Liste de tous les tournois
- Liste des rondes d'un tournoi
- Liste des matchs d'un tournoi

## 🔧 Génération du rapport flake8

Pour vérifier la qualité du code selon les standards PEP 8 :

```bash
# Générer le rapport flake8
flake8 --max-line-length=119 --html --htmldir=flake8_rapport

# Ou simplement afficher les erreurs
flake8 --max-line-length=119
```

Le rapport HTML sera généré dans le dossier `flake8_rapport/`.

## 📊 Spécifications techniques

- **Langage** : Python 3.7+
- **Architecture** : Modèle-Vue-Contrôleur (MVC)
- **Standards** : PEP 8 (ligne max 119 caractères)
- **Base de données** : TinyDB (à implémenter)
- **Interface** : Console (hors ligne)

## 🎯 Fonctionnalités à venir

- 💾 **Sauvegarde/Chargement** : Persistance des données avec TinyDB
- 📤 **Export** : Exportation des rapports en fichiers
- 🔄 **Import** : Importation d'anciens joueurs
- 📈 **Statistiques** : Analyses avancées des performances

## 🐛 Dépannage

### Problèmes courants

1. **Erreur "python not found"**
   - Vérifiez que Python est installé et dans le PATH
   - Utilisez `python3` au lieu de `python` sur Mac/Linux

2. **Erreur d'importation de modules**
   - Vérifiez que l'environnement virtuel est activé
   - Réinstallez les dépendances : `pip install -r requirements.txt`

3. **Erreurs de permissions**
   - Sur Linux/Mac, vous pourriez avoir besoin de `sudo`
   - Vérifiez les permissions d'écriture dans le dossier

### Support

Pour toute question ou problème :
1. Vérifiez ce README
2. Consultez les messages d'erreur dans la console
3. Vérifiez que toutes les dépendances sont installées

## 📝 Notes de développement

- Chaque fichier fait moins de 100 lignes (respect des contraintes)
- Structure MVC claire et modulaire
- Gestion d'erreurs robuste
- Interface utilisateur intuitive
- Code commenté et documenté

## 🏆 Auteur

Développé pour le Centre d'échecs - Application console autonome pour remplacer l'application en ligne instable.
