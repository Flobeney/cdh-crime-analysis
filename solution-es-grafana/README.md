# Solution Elasticsearch + Grafana

Pour cette solution, nous allons utiliser les outils suivants:

- Elasticsearch
- Grafana

## Installation

Il faut évidement avoir ElasticSearch et Grafana installé sur votre machine.

Ensuite, il va falloir créer un venv pour installer les dépendances python.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Il est également possible d'utiliser le makefile pour installer les dépendances.

```bash
make install
```

## Configuration

Il va falloir créer une copie du fichier `.env.example` et le renommer en `.env`.

```bash
cp .env.example .env
```

Il faut ensuite modifier les variables d'environnement pour correspondre à votre configuration.

## Lancement

Il est important de savoir que les scripts Python sont uniquement là pour générer des données dans Elasticsearch.
Il n'y a pas de script pour créer les dashboards dans Grafana.

Pour lancer le script de génération de données, il faut lancer la commande suivante:

```bash
python3 imports_crimes.py
```

ou alors via le makefile:

```bash
make import
```

## Dashboards

Pour les dashboard, il suffit d'importer le fichier `dashboards.json` dans Grafana.

## Nettoyage

Il est également possible de supprimer les données dans Elasticsearch via le script `clean_index_es.py`.

```bash
python3 clean_index_es.py
```

ou alors via le makefile:

```bash
make delete-index
```
