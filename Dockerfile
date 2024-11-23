# Utiliser l'image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000 utilisé par Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
