# 🎵 Music Analysis App

## 📋 Description de l'Application
L'application **Music Analysis App** est une plateforme interactive d'analyse musicale permettant d'explorer des tendances musicales à partir d'un ensemble de données de chansons. L'objectif principal est d'aider à identifier les styles de musique qui maximisent la popularité, en utilisant des analyses visuelles dynamiques et intuitives.

Elle permet :
- D'analyser la popularité des artistes au fil du temps.
- D'explorer la corrélation entre des caractéristiques musicales (tempo, énergie, valence, etc.).
- D'afficher des boxplots et histogrammes dynamiques.
- D'interpréter les données grâce à des visualisations interactives.

---
## Captures d'Écran

### 1. Page d'Accueil

<img width="874" alt="image" src="https://github.com/user-attachments/assets/6b23565e-c339-4318-9279-a512ed0ffe3f" />



### 1. Dashboard
<img width="367" alt="image" src="https://github.com/user-attachments/assets/1b5b2774-e698-417d-b37e-8d8ec9baf460" />



## ⚙️ Instructions d'Installation et d'Exécution

### 1. Prérequis
- Python 3.8 ou version ultérieure
- Git (pour cloner le dépôt)
- Un environnement virtuel Python (recommandé)

### 2. Cloner le dépôt
```bash
git clone https://github.com/elyes0938/music-analysis-app.git
cd music-analysis-app
```

### 3. Créer et activer un environnement virtuel
```bash
# Sous Windows
python -m venv env
env\Scripts\activate

# Sous Linux/MacOS
python3 -m venv env
source env/bin/activate
```

### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 5. Exécuter l'application
```bash
streamlit run app.py
```

Ouvrez votre navigateur sur [http://localhost:8501](http://localhost:8501) pour visualiser l'application.

---

## 🛠️ Choix Techniques

### Langage et Framework
- **Python** : Langage principal pour la manipulation de données et le développement de l'application.
- **Streamlit** : Framework de développement web pour créer des applications interactives de data science rapidement.

### Bibliothèques Utilisées
- **Pandas** : Pour le chargement et la manipulation des données tabulaires.
- **Plotly** : Pour des visualisations interactives et dynamiques (diagrammes, scatter plots, boxplots, etc.).
- **NumPy** : Pour les opérations mathématiques de base (intégré à Pandas).

### Structure du Projet
```
Music_Analysis_App/
├── app.py                  # Code principal de l'application Streamlit
├── data/                   # Dossier contenant le fichier CSV des chansons
├── requirements.txt        # Fichier listant les dépendances Python
└── README.md               # Ce fichier de documentation
```

### Fonctionnalités Clés
- **Dashboard interactif** avec plusieurs types de visualisations.
- **Analyse dynamique** des tendances musicales par artiste et par genre.
- **Exploration des corrélations** entre différentes caractéristiques musicales.

---

## 🚀 Avenir de l'Application
Des améliorations futures peuvent inclure :
- L'ajout de prédictions basées sur des modèles de machine learning.
- L'intégration d'API pour des données musicales en temps réel.
- L'optimisation des performances pour des ensembles de données plus volumineux.

---

### 🤝 Contributions
Les contributions sont les bienvenues ! N'hésitez pas à proposer des suggestions, corriger des bugs ou ajouter de nouvelles fonctionnalités via des *pull requests* sur GitHub.

