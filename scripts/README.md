# Scripts de préparation des données

## Prérequis

```bash
pip install -r requirements-prepare.txt
```

## Exécution

```bash
python scripts/prepare_data.py
```

Ce script effectue les opérations suivantes :

1. **GeoJSON des AOC** : Télécharge le shapefile INAO depuis data.gouv.fr, simplifie les géométries, dissout par appellation, reprojette en WGS84 et sauvegarde en `data/aoc_simplified.geojson`.
   - Si le téléchargement échoue, un GeoJSON de démonstration est généré avec des polygones approximatifs pour les 38 principales AOC.

2. **CSV de production** : Génère `data/production_aoc.csv` avec des volumes de production réalistes par AOC de 2009 à 2019 (basé sur les ordres de grandeur FranceAgriMer publics).
   - Pour utiliser les données Kaggle exactes, téléchargez-les depuis [ce lien](https://www.kaggle.com/datasets/ericnarro/volumes-wine-production-aoc-2009-2019) et placez le CSV dans `data/production_aoc.csv`.

3. **Images d'étiquettes** (optionnel) : Tente de télécharger quelques images depuis HuggingFace. En cas d'échec, l'application utilise un fallback CSS.

## Fichiers générés

| Fichier | Description | Taille cible |
|---------|-------------|--------------|
| `data/aoc_simplified.geojson` | Polygones AOC simplifiés | < 5 MB |
| `data/production_aoc.csv` | Volumes de production 2009-2019 | ~50 KB |
| `assets/labels/*.jpg` | Images d'étiquettes (optionnel) | ~200 KB chacune |
