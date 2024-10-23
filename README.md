# Chatbot avec Langchain et RAG sur un CV

![image](https://github.com/user-attachments/assets/91a2bc20-b7ec-49ad-b0e2-77334678a5ef)


## Description
Ce projet est un chatbot intelligent conçu avec Langchain et Python 3.12. Il utilise la technique RAG (Retrieval-Augmented Generation) pour répondre aux questions basées sur le contenu de ton CV (au format PDF). Le chatbot est capable d'extraire des informations pertinentes de ton CV et de générer des réponses naturelles et précises aux questions des utilisateurs.

Langchain est utilisé pour la construction de la chaîne de traitement des requêtes utilisateur et l'intégration de différentes étapes du flux conversationnel. Le modèle RAG permet d'augmenter les capacités du chatbot en utilisant le contenu d'un PDF (ton CV) comme source de réponses pertinentes.

## Fonctionnalités
- Extraction de contenu pertinent d'un document PDF.
- Réponses augmentées par la génération (RAG) à partir de données de ton CV.
- Utilisation de Langchain pour la gestion du flux conversationnel.
- Support de Python 3.12 pour bénéficier des dernières améliorations du langage.

## Installation
Pour commencer avec ce projet, suis les étapes ci-dessous :

1. **Cloner le dépôt Git**
   ```bash
   git clone https://github.com/Moudathirou/RAG_CHABOT_pdf.git
   cd RAG_CHABOT_pdf
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Sur Windows :
     ```bash
     .\venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
1. **Préparer le fichier PDF**
   - Assure-toi que ton fichier `cv.pdf` est dans le répertoire principal du projet.

2. **Lancer le chatbot**
   - Exécute le script principal pour démarrer le chatbot :
     ```bash
     python app.py
     ```

3. **Interagir avec le chatbot**
   - Le chatbot te permettra de poser des questions concernant ton CV. Par exemple : "Quels sont mes compétences ?", "Quel est mon parcours professionnel ?", etc.

## Technologies Utilisées
- **Langchain** : pour la gestion et l'orchestration des composants du chatbot.
- **Python 3.12** : dernière version de Python, avec des optimisations de performance.
- **RAG (Retrieval-Augmented Generation)** : pour augmenter le générateur de réponses avec des données issues de ton CV.



## Configuration des Dépendances
Voici un exemple de contenu de `requirements.txt` :
```
langchain
openai
PyPDF2
```
Assure-toi d'ajouter toutes les dépendances nécessaires pour que le projet fonctionne correctement.



## Contact
Pour toute question, tu peux me contacter par email à l'adresse : [kymsaindou@gmail.com].


