FROM python:3.10-slim

#  Image de base optimisée
FROM python:3.10-slim

# Installer dépendances système utiles (ex : pour pip, Flask, Mongo)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

#  Créer et définir le dossier de travail
WORKDIR /app

# Copier les dépendances d’abord (meilleur cache Docker)
COPY requirements.txt ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

#  Copier tout le reste du projet
COPY . .

#  Spécifie le port d'écoute de Flask (optionnel mais clair)
EXPOSE 5000

#  Lancer l’application avec Flask (ou Gunicorn si prod)
CMD ["python", "app.py"]
