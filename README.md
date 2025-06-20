# Projet Flask - Authentification & Déploiement Cloud

## Objectif

Ce projet a pour but de créer une application web simple avec **Python Flask**, intégrant un système d'authentification, connectée à une base de données **MongoDB**, containerisée avec **Docker**, puis **déployée automatiquement** avec **GitHub Actions** sur **Render.com**.

---

##  Fonctionnalités principales

-  Authentification avec rôles (`admin`, `utilisateur`)
-  Formulaires : Login / Signup
-  Hash des mots de passe avec Werkzeug
-  Connexion à MongoDB Atlas
-  Variables d’environnement sécurisées avec `.env`
-  Containerisation Docker (Dockerfile + docker-compose)
-  CI/CD automatique avec GitHub Actions
-  Hébergement en ligne avec Render.com
