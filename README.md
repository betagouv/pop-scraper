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

Base POP à scrapper. Seules `memoire` et `palissy` sont supportées. Défault `palissy`

`poetry run scrapy crawl pop_api -a base_pop=memoire`

### `max_items`

Limite le nombre d'objets à parcourir

`poetry run scrapy crawl pop_api -a max_items=200`

### `ref`

Scrappe un seul objet grace à sa référence Palissy

`poetry run scrapy crawl pop_api -a ref=PM72000741`
