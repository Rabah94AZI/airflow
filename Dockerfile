#      Utilisez une    image de base avec Python
FROM python:3.10

# Copiez les fichiers nécessaires dans le conteneur
COPY . /app
WORKDIR /app

# Installez les dépendances
RUN pip install -r requirements.txt

# Exposez le port sur lequel l'application Flask va tourner
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "api.py"]
