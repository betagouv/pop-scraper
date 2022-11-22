# POP Scraper

Aspirateur de données de la [Plateforme Ouverte du Patrimoine](https://www.pop.culture.gouv.fr).

Développé dans le cadre de [Collectif Objets](https://collectif-objets.beta.gouv.fr/)

Codé en Python 3 🐍 avec la librairie [Scrapy](https://docs.scrapy.org/)

## Production

Déployé et disponible sur [zyte.com](https://app.zyte.com/)

## Développement local

- `poetry install`
- `poetry run scrapy crawl pop_api`

## Options

### `base_pop`

Base POP à scrapper. Seules `memoire`, `palissy` et `merimee` sont supportées. Défault `palissy`

`poetry run scrapy crawl pop_api -a base_pop=memoire`

### `max_items`

Limite le nombre d'objets à parcourir

`poetry run scrapy crawl pop_api -a max_items=200`

### `ref`

Scrappe un seul objet grace à sa référence Palissy

`poetry run scrapy crawl pop_api -a ref=PM72000741`

## Scripts

- `make split_csv_by_dpt csv_path=exports/palissy.csv`


## Rajouter une base POP (Joconde, MNR etc)

- récupérer un item en JSON depuis le navigateur sur la page de recherche
- récupérer le CSV de description des champs de la base dans la codebase de POP
- rajouter la classe d'Item dans items.py à partir de ces deux fichiers comparés - la source de vérité est ce qu'on peut récupérer depuis l'API de recherche
